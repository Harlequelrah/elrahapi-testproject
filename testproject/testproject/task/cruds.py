from elrahapi.crud.crud_forgery import CrudForgery
from elrahapi.crud.crud_models import CrudModels
from task.models import Task  # remplacer par l'entité SQLAlchemy
from task.schemas import (  # remplacer par les modèles Pydantic
    TaskCreateModel,
    TaskFullReadModel,
    TaskPatchModel,
    TaskReadModel,
    TaskUpdateModel,
)
from settings.database import database

task_crud_models = CrudModels(
    entity_name="task",
    primary_key_name="id",  # remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Task,  # remplacer par l'entité SQLAlchemy
    ReadModel=TaskReadModel,
    CreateModel=TaskCreateModel,  # Optionel
    UpdateModel=TaskUpdateModel,  # Optionel
    PatchModel=TaskPatchModel,  # Optionel
    FullReadModel=TaskFullReadModel,  # Optionel
)
task_crud = CrudForgery(
    crud_models=task_crud_models, session_manager=database.session_manager
)
