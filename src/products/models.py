from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.repository.models import Base

if TYPE_CHECKING:
    from src.brands.models import Brand


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    price: Mapped[int]
    discount_ratio: Mapped[int]
    description: Mapped[str | None]
    is_active: Mapped[bool]

    age: Mapped[str | None]
    main_ingredient: Mapped[str | None]
    special_prescription: Mapped[str | None]
    country_of_origin: Mapped[str | None]
    packed_in: Mapped[str | None]
    qty_in_package: Mapped[str | None]
    weight: Mapped[str | None]
    length: Mapped[str | None]
    width: Mapped[str | None]
    height: Mapped[str | None]

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    image_id: Mapped[int | None] = mapped_column(ForeignKey("images.id"))
    brand_id: Mapped[id] = mapped_column(ForeignKey("brands.id"))

    brand: Mapped["Brand"] = relationship(back_populates="product")
