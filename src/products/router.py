from fastapi import APIRouter, status

from src.products.schemas import ProductSchema

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("")
async def get_all_products() -> list[ProductSchema]:
    pass


@router.post("/{product_id}")
async def get_product_by_id(id: int) -> ProductSchema:
    pass


@router.post("/{product_name}")
async def get_product_by_name(product_name: str) -> ProductSchema | None:
    pass


@router.post("/{product_is_active}")
async def get_product_by_is_active(is_active: bool) -> list[ProductSchema | None]:
    if not is_active:
        pass
    pass


@router.post("/{brand}")
async def get_products_by_brand(brand: str) -> list[ProductSchema]:
    pass


@router.post("/{category}")
async def get_products_by_category(category: str) -> list[ProductSchema]:
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(
    is_active: bool,
    name: str = None,
    price: int = None,
    discount_ratio: int = None,
    description: str = None,
    category: str = None,
    image_id: int = None,
    brand: str = None,
    characteristics: list[str | None] = None
) -> ProductSchema:
    pass


# TODO: put & patch with dependency from what is required:
@router.post("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(product_id: int) -> ProductSchema:
    pass


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int) -> None:
    pass
