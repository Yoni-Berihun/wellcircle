"""User CRUD operations"""

from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate, UserUpdate
