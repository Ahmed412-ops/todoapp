from sqlalchemy.orm import Session

from app.models.task import Task


class TaskRepository:

    def __init__(self, db: Session):

        self.db = db


    def create(self, task: Task):

        self.db.add(task)

        self.db.commit()

        self.db.refresh(task)

        return task


    def get_user_tasks(
        self,
        user_id: int
    ):

        return self.db.query(Task).filter(
            Task.owner_id == user_id
        ).all()


    def get_by_id_and_owner(
        self,
        task_id: int,
        user_id: int
    ):

        return self.db.query(Task).filter(
            Task.id == task_id,
            Task.owner_id == user_id
        ).first()


    def save(self, task: Task):

        self.db.commit()

        self.db.refresh(task)

        return task


    def delete(self, task: Task):

        self.db.delete(task)

        self.db.commit()