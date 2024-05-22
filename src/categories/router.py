from fastapi import APIRouter, status

from src.categories.schemas import CategorySchema

router = APIRouter(prefix="/categories", tags=["Categories"])


# Get all existing categories
@router.get("")
async def get_all_categories() -> list[CategorySchema]:
    pass


# Get top parent categories with their parent == None or level == 0       ????????????????
@router.get("")
async def get_all_top_categories() -> list[CategorySchema]:
    pass


@router.get("/{parent_id}")
async def get_categories_by_parent(parent_id: int) -> list[CategorySchema]:
    pass


@router.get("/{level}")
async def get_categories_by_level(level: int) -> list[CategorySchema]:
    pass


@router.post("/{category_is_active}")
async def get_category_by_is_active(is_active: bool) -> list[CategorySchema | None]:
    if not is_active:
        pass
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_category(
        is_active: bool,
        level: int,
        name: str = None,
        parent_id: int = None
) -> CategorySchema:
    pass


# TODO: put & patch with dependency from what is required:
@router.post("/{category_id}", status_code=status.HTTP_200_OK)
async def update_category(category_id: int) -> CategorySchema:
    pass


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int) -> None:
    pass
