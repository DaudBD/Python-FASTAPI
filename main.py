from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello StudyFlow"}

@app.get("/add")
def add():
    return {"message": "Hello StudyFlow"}

@app.get("/api")
def api():
    return {"message": "Hello StudyFlow"}