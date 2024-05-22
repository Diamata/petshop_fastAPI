from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.repository.models import Base


class Characteristic(Base):
    __tablename__ = "characteristics"

    name: Mapped[str]
    value_type: Mapped[str]
