from pydantic import BaseModel

from src.core.schemas.enum_characteristics_of_product import CharacteristicsOfProduct


class CharacteristicSchema(BaseModel):
    id: int
    name: CharacteristicsOfProduct
    value_type: [str | None]

    class Config:
        from_attributes = True
