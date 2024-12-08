from fastapi import FastAPI
from router.router_task import router as task


app = FastAPI()
app.include_router(task)
