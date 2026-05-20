from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.user import User

from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskUpdate
)

from app.schemas.common import ApiResponse

from app.auth.jwt_handler import (
    get_current_user
)

from app.services.task_services import (
    create_task as create_task_service,
    get_user_tasks,
    update_task as update_task_service,
    delete_task as delete_task_service
)

from app.utils.response import (
    success_response
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "/",
    response_model=ApiResponse
)
def create_task(
    request: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = create_task_service(
        request=request,
        current_user=current_user,
        db=db
    )

    return success_response(
        message="Task created successfully",
        data=TaskResponse.model_validate(task)
    )


@router.get(
    "/",
    response_model=ApiResponse
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    tasks = get_user_tasks(
        current_user=current_user,
        db=db
    )

    tasks_response = [
        TaskResponse.model_validate(task)
        for task in tasks
    ]

    return success_response(
        message="Tasks fetched successfully",
        data=tasks_response
    )


@router.patch(
    "/{task_id}",
    response_model=ApiResponse
)
def update_task(
    task_id: int,
    request: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = update_task_service(
        task_id=task_id,
        request=request,
        current_user=current_user,
        db=db
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return success_response(
        message="Task updated successfully",
        data=TaskResponse.model_validate(task)
    )


@router.delete(
    "/{task_id}",
    response_model=ApiResponse
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    success = delete_task_service(
        task_id=task_id,
        current_user=current_user,
        db=db
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return success_response(
        message="Task deleted successfully"
    )