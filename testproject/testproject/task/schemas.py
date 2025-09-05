from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from .meta_models import TaskBaseModel


class TaskCreateModel(TaskBaseModel):
    pass


class TaskUpdateModel(TaskBaseModel):
    is_done: bool = Field(example=True)


class TaskPatchModel(TaskBaseModel):
    is_done: bool | None = Field(example=True, default=None)


class TaskReadModel(TaskBaseModel):
    id: int
    date_created: datetime
    date_updated: datetime
    date_deleted: datetime | None = None
    is_done: bool
    is_deleted: bool
    model_config = ConfigDict(from_attributes=True)


class TaskFullReadModel(TaskReadModel):
    model_config = ConfigDict(from_attributes=True)
