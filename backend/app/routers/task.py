from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.task import Task
from app.models.user import User

from app.schemas.task import (
    TaskCreate,
    TaskResponse
)

from app.auth.jwt_handler import (
    get_current_user
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

    task = Task(
        title=request.title,
        description=request.description,
        owner_id=current_user.id
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task

@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    tasks = db.query(Task).filter(
        Task.owner_id == current_user.id
    ).all()

    return tasks