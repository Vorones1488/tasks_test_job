from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.task_router import router as task_api


from src.config import setting
from src.utilit.message_broker.rabbitmq.consumer import make_amqp_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    await make_amqp_consumer(setting)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(task_api)
