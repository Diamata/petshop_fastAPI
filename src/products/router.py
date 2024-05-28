from fastapi import APIRouter, status

from src.products.crud import ProductsRepo
from src.products.schemas import ProductSchema
from src.services.exceptions import NoProductsExistException, NoProductExistsException

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("")
async def get_all_products() -> list[ProductSchema]:
    products = await ProductsRepo.find_all()
    if not products:
        raise NoProductsExistException
    return products


@router.post("/{product_id}")
async def get_product_by_id(product_id: int) -> ProductSchema:
    product = await ProductsRepo.find_by_id(product_id)
    if not product:
        raise NoProductExistsException
    return product


# @router.post("/{product_name}")
# async def get_product_by_name(product_name: str) -> ProductSchema | None:
#     pass
#     # Сделать список продуктов, в которых встречаются такие сочетания
#
#
# @router.post("/{brand}")
# async def get_products_by_brand(brand: str) -> list[ProductSchema]:
#     pass
#
#
# @router.post("/{category}")
# async def get_products_by_category(category: str) -> list[ProductSchema]:
#     pass
#
#
# @router.post("/{product_is_active}")
# async def get_product_by_is_active(is_active: bool) -> list[ProductSchema | None]:
#     if not is_active:
#         pass
#     pass
#
#
# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create_product(
#         is_active: bool,
#         brand_id: int,
#         name: str,
#         price: int,
#         discount_ratio: int,
#         description: str = None,
#         category: str = None,
#         image_id: int = None,
#         age: str = None,
#         main_ingredient: str = None,
#         special_prescription: str = None,
#         country_of_origin: str = None,
#         packed_in: str = None,
#         qty_in_package: int = None,
#         weight: str = None,
#         length: str = None,
#         width: str = None,
#         height: str = None
# ) -> ProductSchema:
#     pass
#
#
# # TODO: put & patch with dependency from what is required:
# @router.post("/{product_id}", status_code=status.HTTP_200_OK)
# async def update_product(product_id: int) -> ProductSchema:
#     pass


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int) -> None:
    product = await ProductsRepo.find_by_id(product_id)
    if not product:
        raise NoProductExistsException
    result = await ProductsRepo.delete_by_id(product_id)
    return result

# TODO: логика для фильтрации
