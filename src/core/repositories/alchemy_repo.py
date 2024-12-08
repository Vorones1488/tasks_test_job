from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound

from src.core.interfaces.interfaces import AbstractRepository
from src.database import async_session_factory
from src.logging.log import log_message


class SQLAlchemyTaskRepository(AbstractRepository):
    model = None

    async def add(self, data: dict) -> model:
        """Adding a task"""
        async with async_session_factory() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            try:
                result = await session.scalars(stmt)
                await session.commit()
                return result.one()
            except IntegrityError as ie:
                log_message("ERROR", f"{str(ie)}")
                session.rollback()

    async def get_id(self, id: int) -> model:
        """Getting one task by id"""
        async with async_session_factory() as session:
            query = select(self.model).filter_by(id=id)
            result = await session.scalars(query)
            try:
                return result.one()
            except NoResultFound as e:
                log_message("ERROR", f"{str(e)}")

            except MultipleResultsFound as e:
                log_message("ERROR", f"{str(e)}")
