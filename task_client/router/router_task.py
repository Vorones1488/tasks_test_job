from fastapi import APIRouter
from fastapi.responses import JSONResponse
from client.task_client import task_client

router = APIRouter()


@router.post(
    "/task_send",
    response_class=JSONResponse,
    summary="добавление задач через очередь сообщений",
)
async def create_task_broker(task_name: str, task_description: str) -> dict:

    await task_client.send_task(task_name, task_description)
    return {"status": "ok"}
