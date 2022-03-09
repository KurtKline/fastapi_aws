from fastapi import FastAPI
from .routers import refugees

from mangum import Mangum

app = FastAPI()

@app.get("/", tags=["Root"])
def read_root()-> dict:
    return {"message": "welcome to FastAPI!"}