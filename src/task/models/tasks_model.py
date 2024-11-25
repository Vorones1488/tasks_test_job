import enum

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.core.model.base import Base

class StatusEnum(enum.Enum):
    new_task = 'Новая задача'
    in_progress = 'В процессе работы'
    completed_successfully = 'Завершено успешно'
    error = 'Ошибка'



class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str] = mapped_column(String(50))
    task_description: Mapped[str] = mapped_column(String(120))

class TaskStatus(Base):
    __tablename__ = 'task_status'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_task: Mapped[int] = mapped_column(ForeignKey('task.id', ondelete='CASCADE'), primary_key=True)
    status: Mapped[StatusEnum]