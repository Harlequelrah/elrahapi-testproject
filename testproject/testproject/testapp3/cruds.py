from elrahapi.crud.crud_forgery import CrudForgery
from elrahapi.crud.crud_models import CrudModels
from testproject.testapp3.models import Entity  # remplacer par l'entité SQLAlchemy
from testproject.testapp3.schemas import (  # remplacer par les modèles Pydantic
    EntityCreateModel,
    EntityFullReadModel,
    EntityPatchModel,
    EntityReadModel,
    EntityUpdateModel,
)
from testproject.settings.database import database_manager

testapp3_crud_models = CrudModels(
    entity_name="testapp3",
    primary_key_name="id",  # remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Entity,  # remplacer par l'entité SQLAlchemy
    ReadModel=EntityReadModel,
    CreateModel=EntityCreateModel,  # Optionel
    UpdateModel=EntityUpdateModel,  # Optionel
    PatchModel=EntityPatchModel,  # Optionel
    FullReadModel=EntityFullReadModel,  # Optionel
)
testapp3_crud = CrudForgery(
    crud_models=testapp3_crud_models, session_manager=database_manager.session_manager
)
