from fastapi import APIRouter, status

from src.brands.schemas import BrandSchema

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("")
async def get_all_brands() -> list[BrandSchema]:
    pass


@router.get("/{brand_name}")
async def get_brand_by_name(brand_name: str) -> BrandSchema:
    pass


@router.get("/{brand_id}")
async def get_brand_by_name(brand_id: int) -> BrandSchema:
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_brand(name: str, description: str = None) -> BrandSchema:
    pass


# TODO: put & patch with dependency from what is required:
@router.post("/{brand_id}", status_code=status.HTTP_200_OK)
async def update_brand(brand_id: int) -> BrandSchema:
    pass


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brand(brand_id: int) -> None:
    pass
