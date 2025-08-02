from pydantic import BaseModel
from typing import List, Optional

class RAGRetrieveRequest(BaseModel):
    query: str
    top_k: Optional[int] = 4

class RetrievedDocument(BaseModel):
    page_content: str
    metadata: dict

class RAGRetrieveResponse(BaseModel):
    retrieved_documents: List[RetrievedDocument]


class Message(BaseModel):
    role: str
    content: str
    
class ChatCompletionRequest(BaseModel):
    model: str = "gemma3:1b"
    messages: List[Message]