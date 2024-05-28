from fastapi import APIRouter, status, Depends

from src.brands.crud import BrandsRepo
from src.brands.dependencies import get_brand_by_id
from src.brands.schemas import BrandSchema, BrandSchemaUpdate
from src.services.exceptions import NoBrandsException, NoBrandException

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("")
async def get_all_brands() -> list[BrandSchema]:
    brand = await BrandsRepo.find_all()
    if not brand:
        raise NoBrandsException
    return brand


@router.post("/id/{brand_id}", response_model=BrandSchema)
async def get_brand_by_id(brand: BrandSchema = Depends(get_brand_by_id)) -> BrandSchema:
    return brand


@router.post("/search/{brand_name}")
async def get_brands_by_partial_name(brand_name: str) -> list[BrandSchema]:
    brand = await BrandsRepo.find_all_by_partial_name(name=brand_name)
    if not brand:
        raise NoBrandException
    return brand


@router.post("/{brand_name}")
async def get_brand_by_name(brand_name: str) -> BrandSchema:
    brand = await BrandsRepo.find_one_or_none_by_name(name=brand_name)
    if not brand:
        raise NoBrandException
    return brand


# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create_brand(name: str, description: str = None) -> BrandSchema:
#     pass


@router.patch("/{brand_id}", status_code=status.HTTP_200_OK)
async def update_brand(
        brand_update: BrandSchemaUpdate,
        brand: BrandSchema = Depends(get_brand_by_id)
) -> BrandSchema:
    result = await BrandsRepo.update_by_id(brand.id, **brand_update.dict())
    return result


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brand(brand: BrandSchema = Depends(get_brand_by_id)) -> None:
    result = await BrandsRepo.delete_by_id(brand.id)
    return result
