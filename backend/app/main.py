from fastapi import FastAPI

from app.database.database import engine, Base
from app.models.user import User
from app.models.task import Task

from app.routers.auth import router as auth_router
from app.routers.task import (
    router as tasks_router
)


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "Todo API Running"}