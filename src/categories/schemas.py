from pydantic import BaseModel, ConfigDict


class CategorySchemaBase(BaseModel):
    name: str
    is_active: bool
    parent_id: int | None


class CategorySchemaUpdate(CategorySchemaBase):
    name: str | None = None
    is_active: bool | None = None
    parent_id: int | None = None
    descendants: list['CategorySchema'] | None = None


class CategoriesWithChildrenSchema(CategorySchemaBase):
    model_config = ConfigDict(from_attributes=True)
    descendants: list['CategorySchema'] = []
    id: int


class CategorySchema(CategorySchemaBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
