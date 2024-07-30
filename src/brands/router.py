from fastapi import APIRouter, status, Depends

from src.brands.crud import BrandsRepo
from src.brands.dependencies import get_brand_by_id
from src.brands.schemas import BrandSchema, BrandSchemaUpdate
from src.services.exceptions import NoBrandsException, NoBrandException, NoBrandCreatedException

router = APIRouter(prefix="/brands", tags=["Brands"])


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_brands() -> list[BrandSchema]:
    brand = await BrandsRepo.find_all()
    if not brand:
        raise NoBrandsException
    return brand


@router.get("/{brand_id}", status_code=status.HTTP_200_OK)
async def get_brand_by_id(brand: BrandSchema = Depends(get_brand_by_id)) -> BrandSchema:
    return brand


@router.get("/search/{brand_name_part}", status_code=status.HTTP_200_OK)
async def get_brands_by_partial_name(brand_name_part: str) -> list[BrandSchema]:
    brand = await BrandsRepo.find_by_partial_name(name=brand_name_part)
    if not brand:
        raise NoBrandException
    return brand


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_brand(name: str, description: str = None) -> BrandSchema:
    brand = await BrandsRepo.create_new_brand(name=name, description=description)
    if not brand:
        raise NoBrandCreatedException
    return brand


@router.patch("/{brand_id}", status_code=status.HTTP_200_OK)
async def update_brand(
        brand_update: BrandSchemaUpdate,
        brand: BrandSchema = Depends(get_brand_by_id)
) -> BrandSchema:
    update_data = brand_update.dict(exclude_unset=True)
    result = await BrandsRepo.update_by_id(brand.id, **update_data)
    return result


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_brand(brand: BrandSchema = Depends(get_brand_by_id)) -> None:
    result = await BrandsRepo.delete_by_id(brand.id)
    return result
