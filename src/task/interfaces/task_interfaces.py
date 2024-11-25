from abc import abstractmethod

from src.core.interfaces.interfaces import AbstractRepository
from src.core.interfaces.models import AbstractModel


class TaskInterface(AbstractRepository):
    @abstractmethod
    async def add(selfl) -> AbstractModel:
        raise NotImplementedError


class TaskStatusInterface(AbstractRepository):
    @abstractmethod
    async def add(selfl) -> AbstractModel:
        raise NotImplementedError