from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import router as api_router
from .services.rag_service import RAGService
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    title="RAG Chatbot Backend for Physical AI Textbook",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
    "*"  # Allow all for deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = RAGService()

@app.on_event("startup")
async def load_documents():
    # Correct absolute path to docs/
    docs_path = os.path.join(BASE_DIR, "docs")

    if not os.path.exists(docs_path):
        print(f"⚠️ Docs folder not found at: {docs_path}")
        return

    files = os.listdir(docs_path)
    mdx_files = [f for f in files if f.endswith(".mdx")]

    if not mdx_files:
        print("⚠️ No MDX files found in docs/. RAG will be empty.")

    for file in mdx_files:
        file_path = os.path.join(docs_path, file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            service.add_document(content)

    print(f"📚 Indexed {len(mdx_files)} MDX files into vector store.")

@app.get("/")
async def health_check():
    return {"message": "Backend is running"}

# Add RAG routes
app.include_router(api_router, prefix="/api")
