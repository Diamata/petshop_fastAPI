from typing import Any

from sqlalchemy import select, delete, insert, update

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
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_by_id(
            cls,
            model_id: int,
            **kwargs: Any
    ) -> model:
        async with async_session_maker() as session:
            stmt_upd = (
                update(cls.model)
                .where(cls.model.id == model_id)
                .values(**kwargs)
            )
            await session.execute(stmt_upd)
            await session.commit()

        stmt = (
            select(cls.model)
            .where(cls.model.id == model_id)
        )

        response = await session.execute(stmt)
        result = response.scalar_one_or_none()
        return result
