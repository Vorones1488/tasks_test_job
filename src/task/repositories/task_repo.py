from sqlalchemy import select, update


from src.core.repositories.alchemy_repo import SQLAlchemyTaskRepository
from src.database import async_session_factory

from src.task.models.tasks_model import Task


from src.task.interfaces.task_interfaces import TaskInterface


class TaskSQLAlchemyRepository(SQLAlchemyTaskRepository, TaskInterface):
    model = Task

    async def get_tasks_with_filter(self, filter_status: str) -> model:
        """Displaying a list of tasks by id with the possible use of a filter by status"""
        async with async_session_factory() as session:
            if filter_status is None:
                qury = select(self.model)
                result = await session.scalars(qury)
                return result.all()
            qury = select(self.model).filter_by(status=filter_status)
            result = await session.scalars(qury)
            return result.all()

    async def put_status_task_to_id(self, id: int, status: str) -> model:
        """Changing the status of a task in the database by id"""
        async with async_session_factory() as session:
            qury = (
                update(self.model)
                .filter_by(id=id)
                .values(status=status)
                .returning(self.model)
            )
            result = await session.scalars(qury)
            await session.commit()
            return result.one()
