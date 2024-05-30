from fastapi import APIRouter, status, Depends

from src.categories.crud import CategoriesRepo
from src.categories.dependencies import get_category_by_id
from src.categories.schemas import CategorySchema, CategoriesWithChildrenSchema
from src.core.schemas.enum_pet_categories import PetsEnum
from src.services.exceptions import NoCategoriesException

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/all_categories")
async def get_all_categories() -> list[CategorySchema]:
    """
    Get all existing categories
    """
    categories = await CategoriesRepo.find_all()
    if not categories:
        raise NoCategoriesException
    return categories


@router.get("/pets")
async def get_all_top_categories() -> list[CategorySchema]:
    """
    Get top parent categories with their parent == None
    """
    categories = await CategoriesRepo.find_top_categories()
    if not categories:
        raise NoCategoriesException
    return categories


@router.get("/{pet}")
async def get_hierarchy_list_of_category_by_pet(pet: PetsEnum) -> dict:
    """
    Get one pet (top) category with its hierarchy
    """
    categories = await CategoriesRepo.find_category_hierarchy(pet)
    if not categories:
        raise NoCategoriesException
    return categories


@router.get("")
async def get_hierarchy_list_of_all_categories() -> list[dict[str, list[CategoriesWithChildrenSchema]]]:
    """
    Get all pet categories with their full hierarchies
    """
    categories = await CategoriesRepo.find_category_hierarchy_full()
    if not categories:
        raise NoCategoriesException
    return categories


@router.post("/{categories_is_active}")
async def get_categories_by_is_active(is_active: bool) -> list[CategorySchema | None]:
    category = await CategoriesRepo.find_all(is_active=is_active)
    if not category:
        raise NoCategoriesException
    return category


@router.patch("", status_code=status.HTTP_200_OK)
async def switch_is_active_of_category_and_children(
        category_id: int,
        activator: bool
) -> dict[str, list[CategoriesWithChildrenSchema]]:
    """
    Switches if the chosen category + all its children active or not
    """
    await CategoriesRepo.switch_accessibility_of_category_and_children(category_id, activator)
    switched_category = await CategoriesRepo.find_category_hierarchy_by_id(category_id)
    return switched_category


# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create_category(
#         is_active: bool = None,
#         name: str = None,
#         parent_id: int = None
# ) -> CategorySchema:
#     pass
#
#
# @router.post("/{category_id}", status_code=status.HTTP_200_OK)
# async def update_category(category_id: int) -> CategorySchema:
#     pass


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category: CategorySchema = Depends(get_category_by_id)) -> None:
    """
    Cascade deletion of a category with its children
    """
    result = await CategoriesRepo.delete_by_id(category.id)
    return result
