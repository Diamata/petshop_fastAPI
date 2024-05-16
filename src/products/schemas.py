from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    title: str
    price: int
    characteristics: list[str]
    description: str

    class Config:
        from_attributes = True
