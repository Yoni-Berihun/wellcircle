"""Booking ORM model"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    provider_id = Column(UUID(as_uuid=True), ForeignKey("providers.id"), nullable=False)
    service_name = Column(String(255), nullable=False)
    slot_datetime = Column(DateTime, nullable=False)
    amount_etb = Column(Integer, nullable=False)
    payment_method = Column(String(50), nullable=False)
    payment_status = Column(String(50), default="pending")
    telebirr_trade_no = Column(String(255), nullable=True, unique=True)
    mpesa_checkout_id = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
