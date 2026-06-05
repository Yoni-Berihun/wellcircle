"""
FastAPI application factory and startup configuration.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, providers, communities, bookings, payments, users
from app.config import settings

app = FastAPI(
    title="WellaTribe API",
    description="Telegram Mini App for wellness providers and communities in Ethiopia",
    version="v1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(providers.router, prefix="/api/providers", tags=["Providers"])
app.include_router(communities.router, prefix="/api/communities", tags=["Communities"])
app.include_router(bookings.router, prefix="/api/bookings", tags=["Bookings"])
app.include_router(payments.router, prefix="/api/payments", tags=["Payments"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "WellaTribe API"}


@app.on_event("startup")
async def startup_event():
    """Startup event handler"""
    print("🚀 WellaTribe API starting...")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler"""
    print("📭 WellaTribe API shutting down...")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
