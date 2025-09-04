from pydantic import BaseModel, Field


class TaskBaseModel(BaseModel):
    name: str = Field(example="Ranger ma chambre")


class TaskInUser(TaskBaseModel):
    pass
