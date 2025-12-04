from fastapi import FastAPI

app = FastAPI(title="FastAPI Backend", version="1.0.0")


@app.get("/health")
async def health_check():
    """Health check endpoint to verify the service is running."""
    return {
        "status": "healthy",
        "service": "fastapi-backend"
    }
