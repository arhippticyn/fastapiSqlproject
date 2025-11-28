from fastapi import FastAPI
from .database import SessionLocal, engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello world'}