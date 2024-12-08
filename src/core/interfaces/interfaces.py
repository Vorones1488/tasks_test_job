from abc import abstractmethod, ABC


from src.core.interfaces.models import AbstractModel


class AbstractRepository(ABC):

    @abstractmethod
    async def add(selfl) -> AbstractModel:
        raise NotImplementedError

    @abstractmethod
    async def get_id(self, id: int) -> AbstractModel:
        raise NotImplementedError
