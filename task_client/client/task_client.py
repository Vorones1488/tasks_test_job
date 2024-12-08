import json
from dataclasses import dataclass
from uuid import uuid4

from config import Settings
from aio_pika import connect_robust, Message


@dataclass
class TaskClient:
    setting: Settings

    async def send_task(self, task_name: str, task_description: str):
        connect = await connect_robust(self.setting.url)
        task = {"task_name": task_name, "task_description": task_description}
        async with connect:
            chanel = await connect.channel()
            message = Message(body=json.dumps(task).encode(), content_type=str(uuid4()))
            await chanel.default_exchange.publish(
                message, routing_key=self.setting.RABBITMQ_QUEUE_TASK
            )


task_client = TaskClient(Settings())
