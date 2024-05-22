from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    price: int
    discount_ratio: int
    description: str
    is_active: bool

    category_id: list[int]
    image_id: int
    brand: str | None
    characteristics: list[str | None]

    class Config:
        from_attributes = True
