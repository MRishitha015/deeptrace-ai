
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from pipeline import DeepTracePipeline


app = FastAPI()


# -------------------------------------
# Enable CORS
# -------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------
# Home Route
# -------------------------------------

@app.get("/")
def home():

    return {
        "message": "DeepTrace AI API Running"
    }


# -------------------------------------
# Detect Route
# -------------------------------------

@app.post("/detect")
async def detect(
    file: UploadFile = File(...)
):

    # ---------------------------------
    # Create uploads folder
    # ---------------------------------

    upload_folder = "uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    # ---------------------------------
    # Save uploaded file
    # ---------------------------------

    file_path = os.path.join(
        upload_folder,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # ---------------------------------
    # Supported extensions
    # ---------------------------------

    image_extensions = (
        ".jpg",
        ".jpeg",
        ".png"
    )

    video_extensions = (
        ".mp4",
        ".avi",
        ".mov",
        ".mkv"
    )

    filename = file.filename.lower()

    # ---------------------------------
    # IMAGE
    # ---------------------------------

    if filename.endswith(
        image_extensions
    ):

        return {

            "message":
            "Image uploaded successfully",

            "file_path":
            file_path,

            "type":
            "image"

        }

    # ---------------------------------
    # VIDEO
    # ---------------------------------

    elif filename.endswith(
        video_extensions
    ):

        pipeline = DeepTracePipeline(
            file_path
        )

        report = pipeline.run()

        return report

    # ---------------------------------
    # UNSUPPORTED FILE
    # ---------------------------------

    else:

        return {

            "error":
            "Unsupported file format"

        }
