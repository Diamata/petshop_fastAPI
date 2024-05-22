from src.brands.models import Brand
from src.repository.crud import BaseRepo


class BrandsRepo(BaseRepo):
    model = Brand
