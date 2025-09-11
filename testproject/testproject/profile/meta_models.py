from pydantic import BaseModel, Field


class ProfileBaseModel(BaseModel):
    profession: str = Field(example="Etudiant")


# class ProfileInProfile2Model(BaseModel):
#     pass
