from fastapi import FastAPI
from src.api.task_router import  router as task




app = FastAPI()
app.include_router(task)


