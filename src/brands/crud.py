from sqlalchemy import select

from src.brands.models import Brand
from src.repository.crud import BaseRepo
from src.repository.db_connection import async_session_maker


class BrandsRepo(BaseRepo):
    model = Brand

    @classmethod
    async def create_new_brand(cls, name: str, description: str):
        async with async_session_maker() as session:
            new_brand = await BrandsRepo.create_new(name=name, description=description)
            stmt = (
                select(Brand)
                .where(Brand.name == name)
            )
            response = await session.execute(stmt)
            result = response.scalar_one_or_none()
            return result
