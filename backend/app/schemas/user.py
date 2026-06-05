"""User request/response schemas"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: Optional[str] = None
    photo_url: Optional[str] = None


class UserCreate(UserBase):
    telegram_id: int


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: str
    telegram_id: int
    points_balance: int
    is_provider: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
