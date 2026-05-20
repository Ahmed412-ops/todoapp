import time
import logging

from fastapi import Request


logger = logging.getLogger("app")


async def logging_middleware(
    request: Request,
    call_next
):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"Status: {response.status_code} "
        f"Time: {process_time:.4f}s"
    )

    return response