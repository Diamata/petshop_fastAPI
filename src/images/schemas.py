from pydantic import BaseModel


class ImageSchema(BaseModel):
    id: int
    url: str
    product_id: int

    class Config:
        from_attributes = True
