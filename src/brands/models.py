from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.repository.models import Base


class Brand(Base):
    __tablename__ = "brands"

    name: Mapped[str]
    description: Mapped[str | None]

