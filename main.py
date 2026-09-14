from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from data_analyzer import analyze_dataset

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


@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    """
    Upload a CSV file and analyze its basic structure.
    """

    if not file.filename.endswith(".csv"):
        return {
            "error": "Please upload a CSV file."
        }

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv"
    )

    try:
        contents = await file.read()
        temp_file.write(contents)
        temp_file.close()

        result = analyze_dataset(temp_file.name)

        return {
            "filename": file.filename,
            "analysis": result
        }

    finally:
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
