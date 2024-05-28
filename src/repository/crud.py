from sqlalchemy import select, delete

from src.repository.db_connection import async_session_maker


class BaseRepo:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            stmt = select(cls.model).filter_by(**filter_by)
            response = await session.execute(stmt)
            result = response.scalars().all()
            return result

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            stmt = select(cls.model).filter_by(id=model_id)
            response = await session.execute(stmt)
            result = response.scalar_one_or_none()
            return result

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            stmt = select(cls.model).filter_by(**filter_by)
            response = await session.execute(stmt)
            result = response.scalar_one_or_none()
            return result

    @classmethod
    async def delete_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            stmt = delete(cls.model).filter_by(id=model_id)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def create_new(cls, **data):
        pass
