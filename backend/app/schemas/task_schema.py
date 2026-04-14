from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: UUID

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    priority: Optional[str]
    assigned_to: Optional[UUID]
    position: Optional[int]

class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: str
    priority: str
    assigned_to: Optional[UUID]
    project_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True