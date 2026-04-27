# api.py - Web API handler

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


