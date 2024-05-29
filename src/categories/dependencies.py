from src.categories.crud import CategoriesRepo
from src.categories.schemas import CategorySchema
from src.services.exceptions import NoCategoryException


async def get_category_by_id(category_id: int) -> CategorySchema:
    category = await CategoriesRepo.find_by_id(model_id=category_id)
    if not category:
        raise NoCategoryException
    return category
