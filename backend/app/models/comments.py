from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid
from datetime import datetime, timezone


class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    content = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
