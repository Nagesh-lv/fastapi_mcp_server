from typing import Dict
from src.fastapi_server.services.rag import RAGService
from fastapi import APIRouter, Depends
router = APIRouter(tags=["Knowledge Base"], prefix="/KB")

# Create a dependency to provide RAGService instance
def get_rag_service():
    return RAGService()

@router.post("/insurance_docs", operation_id="get_insurance_docs")
async def retrieve_documents_for_llm(request: Dict, rag_service: RAGService = Depends(get_rag_service)):
    documents = rag_service.retrieve_docs_only(request, top_k=4)
    return {"retrieved_documents": documents}