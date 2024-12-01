import hashlib

from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

from src.logging.log import log_message
from src.task.interfaces.task_interfaces import TaskInterface
from src.task.repositories.task_repo import TaskSQLAlchemyRepository


class TaskServices:

    def __init__(self, task_repo: TaskInterface) -> None:

        self.task_repo = task_repo()

    async def add_task(self, user_query: BaseModel):
        user_query_dict = user_query.model_dump()
        try:
            result = await self.task_repo.add(user_query_dict)
            return result
        except IntegrityError as e:
            log_message('ERROR', f'ошибка добавления в базу данных {str(e)}')

task_services = TaskServices(TaskSQLAlchemyRepository)



