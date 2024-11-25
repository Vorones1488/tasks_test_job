
from src.core.repositories.alchemy_repo import SQLAlchemyTaskRepository
from src.task.models.tasks_model import Task


from src.task.interfaces.task_interfaces import TaskInterface


class TaskSQLAlchemyRepository(SQLAlchemyTaskRepository, TaskInterface):
    model = Task
    pass

