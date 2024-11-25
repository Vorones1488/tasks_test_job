from abc import abstractmethod, ABC
from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.interfaces.models import AbstractModel


class AbstractRepository(ABC):

    @abstractmethod
    async def add(selfl) -> AbstractModel:
        raise NotImplementedError

    # @abstractmethod
    # async def get(self, id: int) -> Optional[AbstractModel]:
    #     raise NotImplementedError
    #
    # @abstractmethod
    # async def update(self, id: int, model: AbstractModel) -> AbstractModel:
    #     raise NotImplementedError
    #
    # @abstractmethod
    # async def delete(self, id: int) -> None:
    #     raise NotImplementedError
    #
    # @abstractmethod
    # async def list(self) -> List[AbstractModel]:
    #     raise NotImplementedError
