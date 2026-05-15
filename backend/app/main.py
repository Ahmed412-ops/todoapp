from fastapi import FastAPI

from app.database.database import engine, Base
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Todo API Running"}