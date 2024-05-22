from sqlalchemy.orm import Mapped

from src.repository.models import Base


class Characteristic(Base):
    __tablename__ = "characteristics"

    name: Mapped[str]
    value_type: Mapped[str | None]
