from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    workspace_id: UUID

class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    workspace_ud: UUID
    created_by: UUID
    created_at: datetime

    class Config:
        from_attributes = True 