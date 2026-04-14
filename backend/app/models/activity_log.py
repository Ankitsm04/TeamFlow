from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid
from datetime import datetime, timezone

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    action = Column(String, nullable=False)
    entity_type = Column(String) # project, task, comment
    entity_id = Column(UUID(as_uuid=True))

    details = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))