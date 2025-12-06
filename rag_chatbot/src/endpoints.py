from fastapi import APIRouter
from pydantic import BaseModel
from ..services.rag_service import RAGService

router = APIRouter()
service = RAGService()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
async def query_rag(req: QueryRequest):
    return await service.query(req.question)
