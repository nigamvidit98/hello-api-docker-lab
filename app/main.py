from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def health():
    return {"health status": "healthy"}


@app.get("/version")
def version():
    return {"Latest Version": "v1.0.1"}


@app.get("/hostname")
def hostname():
    return {"hostname": socket.gethostname()}


@app.get("/echo")
def echo():
    return {"message": "Hello Human, adding a new endpoint to check conflicts"}

