from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "DeepTrace AI API Running"}
