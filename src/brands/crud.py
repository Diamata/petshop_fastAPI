from sqlalchemy import select, func, update

from src.brands.models import Brand
from src.repository.crud import BaseRepo
from src.repository.db_connection import async_session_maker


class BrandsRepo(BaseRepo):
    model = Brand

    @classmethod
    async def find_all_by_partial_name(cls, name: str):
        async with async_session_maker() as session:
            stmt = (
                select(Brand)
                .where(func.lower(Brand.name).contains(func.lower(name)))
            )
            response = await session.execute(stmt)
            result = response.scalars().all()
            return result

    @classmethod
    async def find_one_or_none_by_name(cls, name: str):
        lowered_name: str = name.lower()
        async with async_session_maker() as session:
            stmt = (
                select(Brand)
                .where(func.lower(Brand.name) == lowered_name)
            )
            response = await session.execute(stmt)
            result = response.scalar_one_or_none()
            return result

    @classmethod
    async def update_by_id(cls, model_id: int, name: str, description: str):
        async with async_session_maker() as session:
            stmt = (
                update(Brand)
                .where(Brand.id == model_id)
                .values(
                    name=name,
                    description=description
                )
            )
            await session.execute(stmt)
            await session.commit()

        stmt_upd = (
            select(Brand)
            .where(Brand.id == model_id)
        )

        response = await session.execute(stmt_upd)
        result = response.scalar_one_or_none()
        return result


