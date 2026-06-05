"""User ORM model"""

from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(Integer, unique=True, nullable=False, index=True)
    username = Column(String(255), nullable=True)
    photo_url = Column(String(500), nullable=True)
    points_balance = Column(Integer, default=0)
    last_checkin_at = Column(DateTime, nullable=True)
    is_provider = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
