from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from src.repository.models import Base

if TYPE_CHECKING:
    from src.products.models import Product


class Brand(Base):
    __tablename__ = "brands"

    name: Mapped[str]
    description: Mapped[str | None]

    product: Mapped["Product"] = relationship(back_populates="brand")
