from fastapi import FastAPI

app = FastAPI(
    title="AI Data Analyst",
    description="An AI-powered platform for intelligent data analysis.",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Data Analyst!",
        "status": "API is running",
        "version": "0.1.0"
    }
