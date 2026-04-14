from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class CommentCreate(BaseModel):
    task_id: UUID
    content: str

class CommentResponse(BaseModel):
    id: UUID
    task_id: UUID
    user_id: UUID
    content: str
    created_at: datetime

    class Config:
        from_attributes = True