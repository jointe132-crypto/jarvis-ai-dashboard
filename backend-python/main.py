from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Lifespan context
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Jarvis Python Backend Starting...")
    yield
    # Shutdown
    logger.info("Jarvis Python Backend Shutting Down...")

# Create FastAPI app
app = FastAPI(
    title="Jarvis AI Services",
    description="AI microservices for Jarvis Dashboard",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoints
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "jarvis-python-backend",
        "version": "1.0.0"
    }

@app.get("/")
async def root():
    return {
        "message": "Jarvis AI Services API",
        "docs": "/docs",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
