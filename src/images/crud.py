from src.images.models import Image
from src.repository.crud import BaseRepo


class ImagesRepo(BaseRepo):
    model = Image
