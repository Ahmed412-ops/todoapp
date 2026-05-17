from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    is_completed: bool | None = None


class TaskResponse(BaseModel):

    id: int
    title: str
    description: str | None
    is_completed: bool

    class Config:
        from_attributes = True