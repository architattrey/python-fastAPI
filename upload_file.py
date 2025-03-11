from fastapi import FastAPI, File, UploadFile, HTTPException
import os

app = FastAPI()

# Define the maximum file size (10MB)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    # Read file content into memory
    file_content = await file.read()
    
    # Check file size
    if len(file_content) > MAX_FILE_SIZE:
        return {"status": "fail", "message": "File size exceeds 10MB limit"}

    return {"status": "success", "filename": file.filename, "size": len(file_content)}

# Run the server: uvicorn filename:app --reload
