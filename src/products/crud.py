from src.products.models import Product
from src.repository.crud import BaseRepo


class ProductsRepo(BaseRepo):
    model = Product
