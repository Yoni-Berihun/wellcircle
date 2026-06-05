"""
Configuration settings for WellaTribe FastAPI application.
Loaded from environment variables.
"""
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # App
    APP_NAME: str = "WellaTribe"
    APP_VERSION: str = "v1.0"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str  # PostgreSQL connection URL
    
    # Telegram
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_API_HASH: str
    TELEGRAM_API_ID: int
    
    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    
    # Payment - Telebirr
    TELEBIRR_MERCHANT_CODE: str = ""
    TELEBIRR_APP_KEY: str = ""
    TELEBIRR_NOTIFY_URL: str = ""
    
    # Payment - M-Pesa
    MPESA_CONSUMER_KEY: str = ""
    MPESA_CONSUMER_SECRET: str = ""
    MPESA_SHORTCODE: str = ""
    MPESA_PASSKEY: str = ""
    MPESA_CALLBACK_URL: str = ""
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://web.telegram.org",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
