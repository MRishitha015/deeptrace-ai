from fastapi import FastAPI, UploadFile, File

import shutil

from pipeline import DeepTracePipeline


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "DeepTrace AI API Running"
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
