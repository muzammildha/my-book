import os
import glob
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from bs4 import BeautifulSoup
from docusaurus_to_text import convert_docusaurus_markdown_to_text # Assuming this utility exists or is created
from ..models.data_models import ChapterContent, Chunk
import uuid

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION_NAME = os.getenv("QDRANT_COLLECTION_NAME", "physical_ai_textbook")

# Initialize Qdrant client
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Initialize embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_text_from_docusaurus_markdown(filepath: str) -> str:
    """Converts Docusaurus-flavored Markdown to plain text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Basic markdown to text conversion (can be improved)
    # Remove frontmatter
    if markdown_content.startswith('---'):
        _, markdown_content = markdown_content.split('---\n', 1)

    # Remove JSX components (simplified)
    markdown_content = BeautifulSoup(markdown_content, 'html.parser').get_text()

    return markdown_content

def chunk_text(text: str, chapter_id: str, chunk_size: int = 500, overlap: int = 50) -> list[Chunk]:
    """Chunks text into smaller pieces with overlap."""
    chunks = []
    words = text.split()
    for i in range(0, len(words), chunk_size - overlap):
        chunk_words = words[i:i + chunk_size]
        chunk_content = ' '.join(chunk_words)
        if chunk_content:
            chunks.append(Chunk(
                id=str(uuid.uuid4()),
                chapter_id=chapter_id,
                content=chunk_content,
                embedding=[] # Will be filled after embedding
            ))
    return chunks

def index_chapters(docs_path: str = "../../physical-ai-textbook/docs"):
    print(f"Indexing chapters from {docs_path}")
    markdown_files = glob.glob(os.path.join(docs_path, "**/*.mdx"), recursive=True)
    markdown_files.extend(glob.glob(os.path.join(docs_path, "**/*.md"), recursive=True))

    if not markdown_files:
        print("No markdown files found in the docs directory. Make sure the path is correct.")
        return

    # Ensure Qdrant collection exists
    try:
        client.recreate_collection(
            collection_name=QDRANT_COLLECTION_NAME,
            vectors_config=models.VectorParams(size=model.get_sentence_embedding_dimension(), distance=models.Distance.COSINE),
        )
        print(f"Recreated Qdrant collection: {QDRANT_COLLECTION_NAME}")
    except Exception as e:
        print(f"Could not recreate Qdrant collection (might already exist): {e}")
        # If it exists, ensure vector params are correct
        collection_info = client.get_collection(collection_name=QDRANT_COLLECTION_NAME).config.vectors_config
        if isinstance(collection_info, models.VectorParams) and (collection_info.size != model.get_sentence_embedding_dimension() or collection_info.distance != models.Distance.COSINE):
            print("WARNING: Existing Qdrant collection has different vector params. Consider dropping and recreating manually.")


    all_points = []
    for filepath in markdown_files:
        chapter_id = os.path.splitext(os.path.basename(filepath))[0] # Use filename as chapter ID
        print(f"Processing chapter: {chapter_id} from {filepath}")

        text_content = get_text_from_docusaurus_markdown(filepath)
        # For simplicity, let's assume the first line is the title if not explicitly in frontmatter
        title = text_content.split('\n', 1)[0].replace('# ', '').strip()
        if not title: # Fallback for files without a clear H1 title at start
            title = chapter_id.replace('-', ' ').title()

        # Store original content in DB (not implemented here, but would be done)
        # chapter_data = ChapterContent(id=chapter_id, title=title, content=text_content, original_content=text_content)
        # Save to Neon Postgres (omitted for brevity)

        chunks = chunk_text(text_content, chapter_id)
        chunk_contents = [c.content for c in chunks]

        if not chunk_contents:
            print(f"No content to chunk for {chapter_id}. Skipping.")
            continue

        # Generate embeddings in batches
        print(f"Generating embeddings for {len(chunk_contents)} chunks...")
        embeddings = model.encode(chunk_contents, show_progress_bar=True).tolist()

        points = []
        for i, chunk in enumerate(chunks):
            chunk.embedding = embeddings[i]
            points.append(models.PointStruct(
                id=str(uuid.uuid4()), # Unique ID for each chunk point
                vector=chunk.embedding,
                payload={
                    "chapter_id": chunk.chapter_id,
                    "content": chunk.content,
                    "filepath": filepath,
                    "title": title # Add title for easier retrieval/citation
                },
            ))
        all_points.extend(points)

    print(f"Upserting {len(all_points)} points to Qdrant collection {QDRANT_COLLECTION_NAME}...")
    # Upsert in batches to avoid large requests
    batch_size = 100
    for i in range(0, len(all_points), batch_size):
        batch = all_points[i:i + batch_size]
        client.upsert(
            collection_name=QDRANT_COLLECTION_NAME,
            wait=True,
            points=batch
        )
    print("Chapter indexing complete.")

if __name__ == "__main__":
    # Assumes script is run from rag_chatbot/ directory
    index_chapters(docs_path="../physical-ai-textbook/docs")
