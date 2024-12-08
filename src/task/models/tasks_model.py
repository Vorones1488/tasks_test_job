from enum import StrEnum

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.core.model.base import Base


class StatusEnum(StrEnum):
    new_task = "Новая задача"
    in_progress = "В процессе работы"
    completed_successfully = "Завершено успешно"
    error = "Ошибка"


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str] = mapped_column(String(50))
    task_description: Mapped[str] = mapped_column(String(120))
    status: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum), server_default=StatusEnum.new_task
    )
