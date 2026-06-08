from datetime import datetime

from app.settings.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Song(Base):
    __tablename__ = "songs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    duration: Mapped[int]
    date_created: Mapped[datetime] = mapped_column(default=func.now())
    date_updated: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(default=False)
    date_deleted: Mapped[datetime|None] = mapped_column(default=None)
