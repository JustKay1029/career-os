from typing import List, Optional
from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class ChunkMetadata(BaseModel):
    doc_id: str = Field(..., description="Unique ID of the parent document")
    filename: str = Field(..., description="Source filename")
    page_number: int = Field(default=1, description="Page number where the chunk originated")
    chunk_index: int = Field(..., description="Sequential index of the chunk within the document")

class DocumentChunk(BaseModel):
    chunk_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique ID for this chunk")
    content: str = Field(..., min_length=1, description="Raw text content of the chunk")
    metadata: ChunkMetadata
    char_count: int = Field(default=0, description="Total characters in this chunk")

    def model_post_init(self, __context):
        if self.char_count == 0:
            self.char_count = len(self.content)

class IngestResponse(BaseModel):
    doc_id: str
    filename: str
    chunks_created: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "success"

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=3, description="Search query or question")
    top_k: int = Field(default=4, ge=1, le=20, description="Number of context chunks to retrieve")
    score_threshold: float = Field(default=0.3, ge=0.0, le=1.0, description="Minimum similarity score")

class Citation(BaseModel):
    doc_id: str
    filename: str
    page_number: int
    excerpt: str
    relevance_score: float

class QueryResponse(BaseModel):
    query: str
    answer: str
    citations: List[Citation]
    latency_ms: float
    grounded: bool = True
