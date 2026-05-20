from sqlalchemy.orm import Session

from app.models.task import Task
from app.models.user import User

from app.schemas.task import (
    TaskCreate,
    TaskUpdate
)

from app.repositories.task_repository import TaskRepository




def create_task(
    request: TaskCreate,
    current_user: User,
    db: Session
):

    repository = TaskRepository(db)
    task = Task(
        title=request.title,
        description=request.description,
        owner_id=current_user.id
    )

    return repository.create(task)


def get_user_tasks(
    current_user: User,
    db: Session
):
    repository = TaskRepository(db)
    return repository.get_user_tasks(
        current_user.id
    )


def update_task(
    task_id: int,
    request: TaskUpdate,
    current_user: User,
    db: Session
):
    repository = TaskRepository(db)
    task = repository.get_by_id_and_owner(
        task_id,
        current_user.id
    )

    if not task:
        return None

    update_data = request.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(task, key, value)

    return repository.save(task)


def delete_task(
    task_id: int,
    current_user: User,
    db: Session
):
    repository = TaskRepository(db)
    task = repository.get_by_id_and_owner(
        task_id,
        current_user.id
    )

    if not task:
        return False

    repository.delete(task)
    return True