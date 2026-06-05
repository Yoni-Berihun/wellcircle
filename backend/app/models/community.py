"""Community ORM models"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
from datetime import datetime
from app.database import Base


class Community(Base):
    __tablename__ = "communities"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider_id = Column(UUID(as_uuid=True), ForeignKey("providers.id"), nullable=False)
    name = Column(String(255), nullable=False)
    category = Column(String(50), nullable=True)
    member_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class CommunityMember(Base):
    __tablename__ = "community_members"
    
    community_id = Column(UUID(as_uuid=True), ForeignKey("communities.id"), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    joined_at = Column(DateTime, default=datetime.utcnow)


class CommunityFeedEvent(Base):
    __tablename__ = "community_feed_events"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    community_id = Column(UUID(as_uuid=True), ForeignKey("communities.id"), nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    event_type = Column(String(50), nullable=False)
    metadata = Column(JSONB, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
