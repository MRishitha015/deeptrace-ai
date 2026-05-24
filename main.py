from fastapi import UploadFile, File


@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "Upload endpoint initialized"
    }
