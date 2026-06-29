from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"status": "v1.0.0"}


@app.get("/hostname")
def hostname():
    return {"hostname": socket.gethostname()}


@app.get("/echo")
def echo():
    return {"message": "Hello Human, adding a new endpoint to echo back a message to understand the flow of the application."}

