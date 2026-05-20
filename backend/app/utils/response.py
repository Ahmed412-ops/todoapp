from app.schemas.common import ApiResponse


def success_response(
    message: str,
    data=None
):

    return ApiResponse(
        success=True,
        message=message,
        data=data
    )