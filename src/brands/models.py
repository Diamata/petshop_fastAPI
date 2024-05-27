from sqlalchemy.orm import Mapped

from src.repository.models import Base
from sqlalchemy.orm import Mapped

from src.repository.models import Base


class Brand(Base):
    __tablename__ = "brands"

    name: Mapped[str]
    description: Mapped[str | None]
