from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from src.repository.models import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    price: Mapped[int]
    discount_ratio: Mapped[int]
    description: Mapped[str | None]
    is_active: Mapped[bool]

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    image_id: Mapped[int] = mapped_column(ForeignKey("images.id"))
    brand_id: Mapped[id] = mapped_column(ForeignKey("brands.id"))
    characteristics_id: Mapped[list[str | None]] = mapped_column(ForeignKey("characteristics.id"))

