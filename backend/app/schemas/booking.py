"""Booking request/response schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookingBase(BaseModel):
    provider_id: str
    service_name: str
    slot_datetime: datetime
    amount_etb: int
    payment_method: str
    phone_number: Optional[str] = None


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    id: str
    user_id: str
    payment_status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
