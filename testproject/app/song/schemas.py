from pydantic import BaseModel, ConfigDict, Field

from datetime import datetime
from decimal import Decimal

from .meta_models import SongBaseModel


class SongCreateModel(SongBaseModel):
    pass


class SongUpdateModel(SongBaseModel):
    pass


class SongPatchModel(BaseModel):
    name:str|None=Field(examples=["Worth it"],default=None)
    name: str | None = Field(examples=[60], default=None)

class SongReadModel(SongBaseModel):
    id: int
    date_created: datetime
    date_updated: datetime
    date_deleted: datetime | None = None
    is_deleted: bool
    model_config = ConfigDict(from_attributes=True)


class SongFullReadModel(SongReadModel):
    model_config = ConfigDict(from_attributes=True)
