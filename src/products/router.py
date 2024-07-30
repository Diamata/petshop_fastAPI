from fastapi import APIRouter, status

from src.products.crud import ProductsRepo
from src.products.schemas import ProductSchema, ProductSchemaUpdate
from src.services.exceptions import NoProductsException, NoProductException, NoProductCreatedException

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_products() -> list[ProductSchema]:
    products = await ProductsRepo.find_all()
    if not products:
        raise NoProductsException
    return products


@router.get("/{product_id}", status_code=status.HTTP_200_OK)
async def get_product_by_id(product_id: int) -> ProductSchema:
    product = await ProductsRepo.find_by_id(product_id)
    if not product:
        raise NoProductException
    return product


@router.get("/search/{product_name_part}", status_code=status.HTTP_200_OK)
async def get_brands_by_partial_name(product_name_part: str) -> list[ProductSchema]:
    product = await ProductsRepo.find_by_partial_name(name=product_name_part)
    if not product:
        raise NoProductException
    return product


# @router.get("/{category}")
# async def get_products_by_category(category: str) -> list[ProductSchema]:
#     pass

# @router.get("/{top_category}")
# async def get_products_by_top_category(top_category: str) -> list[ProductSchema]:
#     pass
#
#
# @router.post("/{product_is_active}")
# async def get_product_by_is_active(is_active: bool) -> list[ProductSchema | None]:
#     pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(
        is_active: bool,
        name: str,
        price: int,
        discount_ratio: int = 1,
        brand_id: int = None,
        description: str = None,
        category_id: int = None,
        image_id: int = None,
        age: str = None,
        main_ingredient: str = None,
        special_prescription: str = None,
        country_of_origin: str = None,
        packed_in: str = None,
        qty_in_package: int = None,
        weight: str = None,
        length: str = None,
        width: str = None,
        height: str = None
) -> ProductSchema:
    await ProductsRepo.create_new(
        is_active=is_active,
        brand_id=brand_id,
        name=name,
        price=price,
        discount_ratio=discount_ratio,
        description=description,
        category_id=category_id,
        image_id=image_id,
        age=age,
        main_ingredient=main_ingredient,
        special_prescription=special_prescription,
        country_of_origin=country_of_origin,
        packed_in=packed_in,
        qty_in_package=qty_in_package,
        weight=weight,
        length=length,
        width=width,
        height=height
    )
    new_category = await ProductsRepo.find_one_or_none(name=name, brand_id=brand_id)
    if not new_category:
        raise NoProductCreatedException
    return new_category


@router.patch("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(
        product_update: ProductSchemaUpdate,
        product_id: int
) -> ProductSchema:
    update_data = product_update.dict(exclude_unset=True)
    result = await ProductsRepo.update_by_id(product_id, **update_data)
    updated_category = await ProductsRepo.find_by_id(product_id)
    return result


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int) -> None:
    product = await ProductsRepo.find_by_id(product_id)
    if not product:
        raise NoProductException
    result = await ProductsRepo.delete_by_id(product_id)
    return result
