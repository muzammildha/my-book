from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import router as api_router
from .services.rag_service import RAGService
import os

app = FastAPI(
    title="RAG Chatbot Backend for Physical AI Textbook",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
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
    # Load MDX documents at startup
    docs_path = "docs"
    for file in os.listdir(docs_path):
        if file.endswith(".mdx"):
            with open(f"{docs_path}/{file}", "r", encoding="utf-8") as f:
                content = f.read()
                service.add_document(content)

    print("📚 All MDX files indexed into vector store.")

@app.get("/")
async def health_check():
    return {"message": "Backend is running"}

# Add RAG routes
app.include_router(api_router, prefix="/api")
