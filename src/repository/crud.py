from sqlalchemy import select

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
        pass

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        pass

    @classmethod
    async def delete_by_id(cls, model_id):
        pass

    @classmethod
    async def create_new(cls, **data):
        pass

    @classmethod
    async def update_by_id(cls, model_id):
        pass
