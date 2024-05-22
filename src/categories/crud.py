from src.categories.models import Category
from src.repository.crud import BaseRepo


class CategoriesRepo(BaseRepo):
    model = Category
