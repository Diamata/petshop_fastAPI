from pydantic import BaseModel


class CharacteristicSchema(BaseModel):
    id: int
    name: str
    value_type: str

    class Config:
        from_attributes = True
