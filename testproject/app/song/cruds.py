from app.song.models import Song  # remplacer par l'entité SQLAlchemy
from app.song.schemas import (  # remplacer par les modèles Pydantic
    SongCreateModel,
    SongFullReadModel,
    SongPatchModel,
    SongReadModel,
    SongUpdateModel,
)
from app.settings.config.database_config import session_manager
from elrahapi.crud.crud_forgery import CrudForgery
from elrahapi.crud.crud_models import CrudModels

song_crud_models = CrudModels(
    entity_name="song",
    primary_key_name="id",  # remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Song,  # remplacer par l'entité SQLAlchemy
    ReadModel=SongReadModel,
    CreateModel=SongCreateModel,  # Optionel
    UpdateModel=SongUpdateModel,  # Optionel
    PatchModel=SongPatchModel,  # Optionel
    FullReadModel=SongFullReadModel,  # Optionel
)
song_crud = CrudForgery(crud_models=song_crud_models, session_manager=session_manager)
