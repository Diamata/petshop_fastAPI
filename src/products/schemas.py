from pydantic import BaseModel, ConfigDict


class ProductSchemaBase(BaseModel):
    name: str
    price: int
    discount_ratio: int
    description: str | None
    is_active: bool

    age: str | None
    main_ingredient: str | None
    special_prescription: str | None
    country_of_origin: str | None
    packed_in: str | None
    qty_in_package: str | None
    weight: str | None
    length: str | None
    width: str | None
    height: str | None

    category_id: int
    image_id: int | None
    brand_id: int | None


class ProductSchemaUpdate(ProductSchemaBase):
    name: str | None = None
    price: int | None = None
    discount_ratio: int | None = None
    description: str | None = None
    is_active: bool | None = None

    age: str | None = None
    main_ingredient: str | None = None
    special_prescription: str | None = None
    country_of_origin: str | None = None
    packed_in: str | None = None
    qty_in_package: str | None = None
    weight: str | None = None
    length: str | None = None
    width: str | None = None
    height: str | None = None

    category_id: int | None = None
    image_id: int | None = None
    brand_id: int | None = None


class ProductSchema(ProductSchemaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
