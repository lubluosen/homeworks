from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index_page():
    return {"Greatings": "Hello, World!"}


@app.get("/ping/")
def ping_page():
    return {"message": "pong"}
