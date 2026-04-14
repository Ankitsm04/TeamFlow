from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid
from datetime import datetime, timezone

class WorkspaceMember(Base):
    __tablename__ = "workspace_members"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    role = Column(String, default="member")

    joined_at = Column(DateTime, default=datetime.now(timezone.utc))