from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid
from datetime import datetime, timezone

class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)

    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.now(timezone.utc))