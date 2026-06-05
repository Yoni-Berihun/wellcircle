"""Provider request/response schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProviderBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    location_text: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    price_range: Optional[str] = None
    rating: Optional[float] = None
    cover_photo_url: Optional[str] = None


class ProviderCreate(ProviderBase):
    pass


class ProviderResponse(ProviderBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class ProviderStatsResponse(BaseModel):
    total_members: int
    new_joins_today: int
    bookings_this_week: int
    revenue_etb: float
