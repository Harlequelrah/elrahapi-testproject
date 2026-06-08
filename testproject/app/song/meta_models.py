from pydantic import BaseModel, Field

class SongBaseModel(BaseModel):
    name: str = Field(examples=["Worth it"])
    duration: int = Field(examples=[60])
