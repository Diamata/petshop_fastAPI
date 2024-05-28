from src.brands.crud import BrandsRepo
from src.brands.schemas import BrandSchema
from src.services.exceptions import NoBrandException


async def get_brand_by_id(brand_id: int) -> BrandSchema:
    brand = await BrandsRepo.find_by_id(model_id=brand_id)
    if not brand:
        raise NoBrandException
    return brand
