from fastapi import FastAPI, Request, HTTPException

from app.database.database import engine, Base
from app.models.user import User
from app.models.task import Task

from app.routers.auth import router as auth_router
from app.routers.task import router as tasks_router

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.core.exception import http_exception_handler, validation_exception_handler

from app.core.logging import (
    setup_logging
)

from app.middleware.logging_middleware import (
    logging_middleware
)


app = FastAPI()

setup_logging()

app.middleware("http")(
    logging_middleware
)

app.include_router(auth_router)
app.include_router(tasks_router)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

@app.get("/")
def root():
    return {"message": "Todo API Running"}