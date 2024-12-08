from typing import List

from fastapi import APIRouter

from src.task.models.tasks_model import StatusEnum
from src.task.schemas.task_schemas import TaskResponseSchemas, TaskBaseSchemas
from src.task.services.task_services import task_services

router = APIRouter(prefix="/task", tags=["Задачи"])


@router.post(
    "/",
    response_model=TaskResponseSchemas,
    summary="добавление задачи",
    description="Добавляет новую задачу в базу данных",
)
async def add_task(request: TaskBaseSchemas):
    result = await task_services.add_task(request)
    return result


@router.get(
    "/{id:int}",
    response_model=TaskResponseSchemas,
    summary="получение задачи по его id",
    description="получение задачи по ее id",
)
async def get_task_id(id: int):
    result = await task_services.get_task_id(id)
    return result


@router.get(
    "/",
    response_model=List[TaskResponseSchemas],
    summary="получение всех задач",
    description="получение всех задач с возосжностью фильтрации по статусу",
)
async def get_tasks(filter_by_status: StatusEnum = None):
    result = await task_services.get_tasks_filter_by_status(filter_by_status)
    return result
