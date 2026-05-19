from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.auth.jwt_handler import get_current_user

from app.services.task_service import (
    create_task as create_task_service,
    get_user_tasks,
    update_task as update_task_service,
    delete_task as delete_task_service
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post(
    "/",
    response_model=TaskResponse
)
def create_task(
    request: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_task_service(
        request=request,
        current_user=current_user,
        db=db
    )

@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_user_tasks(
        current_user=current_user,
        db=db
    )
    

@router.patch(
    "/{task_id}",
    response_model=TaskResponse
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

    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    success= delete_task_service(
        task_id=task_id,
        current_user=current_user,
        db=db
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }