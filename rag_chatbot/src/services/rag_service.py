from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from openai import OpenAI
import uuid

class RAGService:
    def __init__(self):
        # Connect Qdrant
        self.qdrant = QdrantClient(":memory:")  # OR your cloud URL

        # Create collection
        self.qdrant.recreate_collection(
            collection_name="docs",
            vectors_config={"size": 1536, "distance": "Cosine"}
        )

        # OpenAI client
        self.client = OpenAI()

    def embed(self, text: str):
        res = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
        )
        return res.data[0].embedding

    def add_document(self, text: str):
        vec = self.embed(text)

        self.qdrant.upsert(
            collection_name="docs",
            points=[
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vec,
                    payload={"text": text},
                )
            ],
        )

    async def query(self, text: str, selected_context=None):
        query_vec = self.embed(text)

        search = self.qdrant.search(
            collection_name="docs",
            query_vector=query_vec,
            limit=3
        )

        context = "\n".join(hit.payload["text"] for hit in search)

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Answer using the provided context."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{text}"},
            ]
        )

        return {
            "answer": response.choices[0].message.content,
            "sources": [hit.payload["text"] for hit in search],
        }
