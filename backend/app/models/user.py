import uuid
from sqlalchemy import Column, Integer, String
from app.database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    security_stamp = Column(String,unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    tasks = relationship("Task", back_populates="owner")