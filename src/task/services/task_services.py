import json
from types import NoneType
from typing import List

import aio_pika
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound
from fastapi.exceptions import HTTPException
from fastapi import status

from src.logging.log import log_message
from src.task.interfaces.task_interfaces import TaskInterface
from src.task.models.tasks_model import Task
from src.task.repositories.task_repo import TaskSQLAlchemyRepository
from src.task.schemas.task_schemas import TaskBaseSchemas


class TaskServices:

    def __init__(self, task_repo: TaskInterface) -> None:

        self.task_repo = task_repo()

    async def add_task(self, user_query: BaseModel) -> Task:
        user_query_dict = user_query.model_dump()
        try:
            result = await self.task_repo.add(user_query_dict)
            return result
        except IntegrityError as e:
            log_message("error", f"ошибка добавления в базу данных {str(e)}")
            raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED)

    async def get_task_id(self, id: int) -> Task:
        """Service for receiving tasks by id"""
        try:
            result = await self.task_repo.get_id(id)
            return result
        except NoResultFound:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        except MultipleResultsFound:
            raise HTTPException(status.HTTP_207_MULTI_STATUS)

    async def get_tasks_filter_by_status(self, status_task: str) -> List[Task]:
        """Service for receiving all tasks or tasks by status filter"""
        result = await self.task_repo.get_tasks_with_filter(status_task)
        return result


task_services = TaskServices(TaskSQLAlchemyRepository)
