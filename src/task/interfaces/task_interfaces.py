from abc import abstractmethod

from src.core.interfaces.interfaces import AbstractRepository
from src.core.interfaces.models import AbstractModel


class TaskInterface(AbstractRepository):
    @abstractmethod
    async def add(selfl) -> AbstractModel:
        raise NotImplementedError

    @abstractmethod
    async def get_id(self, id: int) -> AbstractModel:
        raise NotImplementedError

    @abstractmethod
    async def get_tasks_with_filter(self,filter_status:str) -> AbstractModel:
        raise NotImplementedError