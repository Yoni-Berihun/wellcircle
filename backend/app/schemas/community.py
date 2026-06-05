"""Community request/response schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CommunityBase(BaseModel):
    name: str
    category: Optional[str] = None


class CommunityCreate(CommunityBase):
    provider_id: str


class CommunityResponse(CommunityBase):
    id: str
    provider_id: str
    member_count: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class CommunityFeedEventResponse(BaseModel):
    id: str
    user_id: str
    event_type: str
    metadata: Optional[dict] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
