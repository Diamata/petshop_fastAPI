from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.repository.models import Base


class Image(Base):
    __tablename__ = "images"

    url: Mapped[str]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
