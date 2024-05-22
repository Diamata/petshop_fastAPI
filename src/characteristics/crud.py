from src.characteristics.models import Characteristic
from src.repository.crud import BaseRepo


class CharacteristicsRepo(BaseRepo):
    model = Characteristic
