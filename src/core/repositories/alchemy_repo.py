from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from src.core.interfaces.interfaces import AbstractRepository
from src.database import async_session_factory
from src.logging.log import log_message



class SQLAlchemyTaskRepository(AbstractRepository):
    model = None

    async def add(self, data: dict) -> model:
        async with async_session_factory() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            try:
                result =  await session.scalars(stmt)
                await session.commit()
                return result.one()
            except IntegrityError as ie:
                log_message('ERROR', f'{str(ie)}')
                session.rollback()




    async def get_id(self, id: int) -> model:
        async with async_session_factory() as session:
            qury = select(self.model).filter_by(id=id)
            result = await session.scalars(qury)
            return result.one()
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
