from sqlalchemy.orm import Session

from app.models.task import Task
from app.models.user import User

from app.schemas.task import (
    TaskCreate,
    TaskUpdate
)


def create_task(
    request: TaskCreate,
    current_user: User,
    db: Session
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


def get_user_tasks(
    current_user: User,
    db: Session
):

    tasks = db.query(Task).filter(
        Task.owner_id == current_user.id
    ).all()

    return tasks


def update_task(
    task_id: int,
    request: TaskUpdate,
    current_user: User,
    db: Session
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        return None

    update_data = request.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()

    db.refresh(task)

    return task


def delete_task(
    task_id: int,
    current_user: User,
    db: Session
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        return False

    db.delete(task)

    db.commit()

    return True