from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.repository.models import Base


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str]
    is_active: Mapped[bool]

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))
