from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "DeepTrace AI API Running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "v0.1"}
