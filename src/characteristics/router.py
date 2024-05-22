from fastapi import APIRouter, status

from src.characteristics.schemas import CharacteristicSchema

router = APIRouter(prefix="/characteristics", tags=["Characteristics"])


@router.get("")
async def get_all_characteristics() -> list[CharacteristicSchema]:
    pass


@router.get("/{characteristic_type}")
async def get_characteristic_by_name(characteristic_type: str) -> list[CharacteristicSchema]:
    pass


@router.get("/{characteristics_id}")
async def get_characteristic_by_id(characteristics_id: int) -> CharacteristicSchema:
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_characteristic(name: str, value_type: str) -> CharacteristicSchema:
    pass


# TODO: put & patch with dependency from what is required:
@router.post("/{characteristic_id}", status_code=status.HTTP_200_OK)
async def update_characteristic(characteristic_id: int) -> CharacteristicSchema:
    pass


@router.delete("/{characteristic_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_characteristic(characteristic_id: int) -> None:
    pass
