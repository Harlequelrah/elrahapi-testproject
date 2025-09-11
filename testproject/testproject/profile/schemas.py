from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from .meta_models import ProfileBaseModel


class ProfileCreateModel(ProfileBaseModel):
    pass


class ProfileUpdateModel(ProfileBaseModel):
    pass


class ProfilePatchModel(BaseModel):
    profession: str | None = Field(example="Etudiant", default=None)


class ProfileReadModel(ProfileBaseModel):
    id: int
    date_created: datetime
    date_updated: datetime
    date_deleted: datetime | None = None
    is_deleted: bool
    model_config = ConfigDict(from_attributes=True)


class ProfileFullReadModel(ProfileReadModel):
    model_config = ConfigDict(from_attributes=True)
