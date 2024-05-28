from pydantic import BaseModel, ConfigDict


class BrandSchemaBase(BaseModel):
    name: str
    description: str | None


class BrandSchemaUpdate(BrandSchemaBase):
    name: str | None = None
    description: str | None = None


class BrandSchema(BrandSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
