from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    price: int
    discount_ratio: int
    description: str
    is_active: bool

    age: str | None
    main_ingredient: str | None
    special_prescription: str | None
    country_of_origin: str | None
    packed_in: str | None
    qty_in_package: int | None
    weight: str | None
    length: str | None
    width: str | None
    height: str | None

    category_id: list[int]
    image_id: int
    brand: str | None
    characteristics: list[str | None]

    class Config:
        from_attributes = True
