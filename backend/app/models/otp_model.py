from sqlalchemy import Column, String, DateTime
from app.db.database import Base

class OTP(Base):
    __tablename__ = "otps"

    email = Column(String, primary_key=True, index=True)
    otp = Column(String, nullable=False)
    expires_in = Column(DateTime(timezone=True), nullable=False) 