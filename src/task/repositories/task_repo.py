from sqlalchemy import select

from src.core.repositories.alchemy_repo import SQLAlchemyTaskRepository
from src.database import async_session_factory
from src.task.models.tasks_model import Task


from src.task.interfaces.task_interfaces import TaskInterface


class TaskSQLAlchemyRepository(SQLAlchemyTaskRepository, TaskInterface):
    model = Task
    async def get_tasks_with_filter(self, filter_status:str) -> model:
        async with async_session_factory() as session:
            if filter_status is None:
                qury = select(self.model)
                result = await session.scalars(qury)
                return result.all()
            qury = select(self.model).filter_by(status=filter_status)
            result = await session.scalars(qury)
            return result.all()




