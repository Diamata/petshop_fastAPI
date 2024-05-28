from sqlalchemy import select

from src.brands.models import Brand
from src.products.models import Product
from src.repository.crud import BaseRepo
from src.repository.db_connection import async_session_maker


class ProductsRepo(BaseRepo):
    model = Product

    @classmethod
    async def find_all(cls, **filter_by):
        """
        SELECT products.*, brands.name as brand
            FROM products
        LEFT JOIN brands ON products.brand_id = brands.id
        """
        async with async_session_maker() as session:
            stmt = (
                select(Product, Brand.name.label('brand'))
                .outerjoin(Brand, Product.brand_id == Brand.id)
            )

            response = await session.stream(stmt)

            products_with_brand = []

            async for row in response:
                product, brand = row
                product_dict = {**product.__dict__, 'brand': brand}
                product_dict = {k: v for k, v in product_dict.items() if not k.startswith('_')}
                products_with_brand.append(product_dict)

            return products_with_brand

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            stmt = (
                select(Product, Brand.name.label('brand'))
                .where(Product.id == model_id)
                .outerjoin(Brand, Product.brand_id == Brand.id)
            )

            response = await session.stream(stmt)

            product_with_brand = {}

            async for row in response:
                product, brand = row
                product_with_brand = {**product.__dict__, 'brand': brand}
                product_with_brand = {k: v for k, v in product_with_brand.items() if not k.startswith('_')}

            return product_with_brand

