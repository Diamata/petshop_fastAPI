from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

intpk = Annotated[int, mapped_column(primary_key=True, nullable=False, autoincrement=True)]


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[intpk]
