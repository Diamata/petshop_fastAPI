from sqlalchemy import select, func

from src.categories.models import Category
from src.categories.schemas import CategoriesWithChildrenSchema
from src.core.schemas.enum_pet_categories import PetsEnum
from src.repository.crud import BaseRepo
from src.repository.db_connection import async_session_maker
from src.services.exceptions import NoCategoryException


class CategoriesRepo(BaseRepo):
    model = Category

    @classmethod
    async def find_top_categories(cls):
        async with async_session_maker() as session:
            stmt = (
                select(Category)
                .where(Category.parent_id == None)
            )
            response = await session.execute(stmt)
            result = response.scalars().all()
            return result

    @classmethod
    async def get_category_with_children(cls, category_id: int) -> CategoriesWithChildrenSchema:
        async with async_session_maker() as session:
            category_query = select(Category).where(Category.id == category_id)
            response = await session.execute(category_query)
            category = response.scalar_one_or_none()

            if category is None:
                raise NoCategoryException

            category_data = CategoriesWithChildrenSchema.from_orm(category)

            children_query = select(Category).where(Category.parent_id == category_id)
            response = await session.execute(children_query)
            child_result = response.scalars().all()

            for child in child_result:
                child_data = await cls.get_category_with_children(child.id)
                category_data.children.append(child_data)

            return category_data

    @classmethod
    async def find_category_hierarchy(cls, pet: PetsEnum) -> dict[str, list[CategoriesWithChildrenSchema]]:
        pet_lower = pet.name.lower()
        async with async_session_maker() as session:
            category_hierarchy = {
                pet_lower: []
            }

            pet_selected = select(Category).where(Category.name == pet_lower).cte("pet_selected")

            first_line_children = select(Category).where(Category.parent_id == pet_selected.c.id)

            response = await session.execute(first_line_children)
            first_line_result = response.scalars().all()

            for child in first_line_result:
                child_data = await cls.get_category_with_children(child.id)
                category_hierarchy[pet_lower].append(child_data)

            return category_hierarchy

    @classmethod
    async def find_category_hierarchy_full(cls) -> list[dict[str, list[CategoriesWithChildrenSchema]]]:
        async with async_session_maker() as session:
            categories_list = []

            stmt = select(Category).where(Category.parent_id == None)

            response = await session.execute(stmt)
            pet_categories = response.scalars().all()

            for category in pet_categories:
                item = await cls.find_category_hierarchy(category)
                categories_list.append(item)
            return categories_list


