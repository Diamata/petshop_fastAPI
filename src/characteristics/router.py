from fastapi import APIRouter, status

from src.characteristics.schemas import CharacteristicSchema
from src.core.schemas.enum_characteristics_of_product import CharacteristicsOfProduct

router = APIRouter(prefix="/characteristics", tags=["Characteristics"])


@router.get("")
async def get_all_characteristics() -> list[CharacteristicSchema]:
    pass


@router.get("/{characteristics_type}")
async def get_characteristics_by_type(characteristic_type: str) -> list[CharacteristicSchema]:
    pass


@router.get("/{characteristic_id}")
async def get_characteristic_by_id(characteristic_id: int) -> CharacteristicSchema:
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_characteristic(name: CharacteristicsOfProduct, value_type: str) -> CharacteristicSchema:
    pass


# TODO: put & patch with dependency from what is required:
@router.post("/{characteristic_id}", status_code=status.HTTP_200_OK)
async def update_characteristic(characteristic_id: int) -> CharacteristicSchema:
    pass


@router.delete("/{characteristic_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_characteristic(characteristic_id: int) -> None:
    pass
