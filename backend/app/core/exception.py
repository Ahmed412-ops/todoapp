from fastapi import (
    Request,
    HTTPException
)

from fastapi.responses import JSONResponse

from fastapi.exceptions import (
    RequestValidationError
)


async def http_exception_handler(
    request: Request,
    exc: HTTPException
):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "errors": []
        }
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    errors = []

    for error in exc.errors():

        field = ".".join(
            map(str, error["loc"])
        )

        errors.append(
            f"{field}: {error['msg']}"
        )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation error",
            "errors": errors
        }
    )