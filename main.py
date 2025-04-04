from fastapi import FastAPI
from src.api.endpoints import router

app = FastAPI(title="Hotel Booking RAG API")

@app.get("/")
async def root():
    return {"message": "API is running"}

# Register API endpoints
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
