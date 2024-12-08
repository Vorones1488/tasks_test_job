import json
import random
from time import sleep
from typing import Any

import aio_pika

from src.logging.log import log_message
from src.task.interfaces.task_interfaces import TaskInterface
from src.task.models.tasks_model import Task, StatusEnum

from src.task.repositories.task_repo import TaskSQLAlchemyRepository
from src.task.schemas.task_schemas import TaskBaseSchemas


class Worker:
    def __init__(self, task_repo: TaskInterface):
        self.task_repo = task_repo()

    async def task_processing(self, model: Task, status: str):
        await self.task_repo.put_status_task_to_id(model.id, status)

    @staticmethod
    def random_status() -> str:
        time = random.randint(5, 10)
        sleep(time)
        success = random.choice([True, False])
        if success:
            return StatusEnum.completed_successfully
        return StatusEnum.error

    async def add_task_broke(self, task: TaskBaseSchemas) -> Any:
        "Receiving a task from a queue and processing it"
        user_query_dict = task.model_dump()

        result = await self.task_repo.add(user_query_dict)
        log_message("info", f"Задача {result.task_name} в работе")
        await self.task_processing(result, StatusEnum.in_progress)
        status = self.random_status()
        log_message("info", f"задача {result.task_name}")
        await self.task_processing(result, status)

    async def consume_task(self, message: aio_pika.IncomingMessage):
        """Receiving messages from a queue"""

        async with message.process(requeue=True):
            task_body = TaskBaseSchemas(**json.loads(message.body.decode()))
            corelation_id = message.correlation_id
            await self.add_task_broke(task_body)


worker = Worker(TaskSQLAlchemyRepository)
