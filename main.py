from fastapi import FastAPI, UploadFile, File
import shutil
from datetime import datetime

from pipeline import DeepTracePipeline


app = FastAPI(
    title="DeepTrace AI",
    description="AI-powered deepfake forensic detection system",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "DeepTrace AI API Running"
    }


@app.get("/health")
def health_check():

    return {
        "status": "running",
        "timestamp": str(datetime.now())
    }


@app.get("/info")
def info():

    return {
        "project": "DeepTrace AI",
        "type": "Deepfake Detection System",
        "version": "1.0.0"
    }


@app.post("/detect")
async def detect_deepfake(
    file: UploadFile = File(...)
):

    video_path = file.filename

    with open(video_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    pipeline = DeepTracePipeline(
        video_path
    )

    report = pipeline.run()

    return report
