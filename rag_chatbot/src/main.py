from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Assuming these modules will be created later
# from .api import endpoints
# from .services import rag_service

app = FastAPI(
    title="RAG Chatbot Backend for Physical AI Textbook",
    description="FastAPI backend for the Retrieval-Augmented Generation chatbot, personalization, and translation features.",
    version="1.0.0",
)

# Configure CORS
origins = [
    "http://localhost:3000",  # Docusaurus frontend development server
    # Add your GitHub Pages URL here in production, e.g., "https://your-github-username.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
async def read_root():
    return {"message": "RAG Chatbot Backend is running"}

# Include API endpoints (uncomment when created)
# app.include_router(endpoints.router)
