from pydantic import BaseModel, Field

from src.task.models.tasks_model import StatusEnum


class TaskBaseSchemas(BaseModel):
    task_name:str = Field(..., max_length=50)
    task_description: str = Field(..., max_length=120)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "task_name": "Название задачи мксимум 50 символов",
                    "task_description": "Описание задачи максимум 120 символов"
                }
            ]
        }

class TaskResponseSchemas(TaskBaseSchemas):
    id: int
    status: str