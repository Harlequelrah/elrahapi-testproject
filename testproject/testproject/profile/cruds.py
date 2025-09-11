from profile.models import Profile  # remplacer par l'entité SQLAlchemy
from profile.schemas import (  # remplacer par les modèles Pydantic
    ProfileCreateModel,
    ProfileFullReadModel,
    ProfilePatchModel,
    ProfileReadModel,
    ProfileUpdateModel,
)

from elrahapi.crud.crud_forgery import CrudForgery
from elrahapi.crud.crud_models import CrudModels
from settings.database import database

myapp_crud_models = CrudModels(
    entity_name="profile",
    primary_key_name="id",  # remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Profile,  # remplacer par l'entité SQLAlchemy
    ReadModel=ProfileReadModel,
    CreateModel=ProfileCreateModel,  # Optionel
    UpdateModel=ProfileUpdateModel,  # Optionel
    PatchModel=ProfilePatchModel,  # Optionel
    FullReadModel=ProfileFullReadModel,  # Optionel
)
profile_crud = CrudForgery(
    crud_models=myapp_crud_models, session_manager=database.session_manager
)
