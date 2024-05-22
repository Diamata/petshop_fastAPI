from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    name: str
    level: int
    is_active: bool
    parent_id: int | None

    class Config:
        from_attributes = True
