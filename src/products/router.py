from fastapi import APIRouter

from src.products.schemas import ProductSchema

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("")
async def get_all_products() -> list[ProductSchema]:
    pass


@router.post("/{product_id}")
async def get_product_by_id(id: int) -> ProductSchema:
    pass


@router.post("/{product_title}")
async def get_product_by_title(product_title: str) -> ProductSchema:
    pass


@router.delete("/{product_id}")
async def delete_product(product_id: int) -> None:
    pass


@router.post("/{product_id}")
async def update_product(product_id: int) -> ProductSchema:
    # TODO: put & patch with dependency from what is required
    pass

