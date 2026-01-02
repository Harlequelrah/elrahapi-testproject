from elrahapi.crud.crud_forgery import CrudForgery
from elrahapi.crud.crud_models import CrudModels
from testproject.settings.database import database_manager
from testproject.settings.logger.model import LogModel
from testproject.settings.logger.schema import LogReadModel
log_crud_models = CrudModels (
    entity_name='log',
    primary_key_name='id',
    SQLAlchemyModel=LogModel,
    ReadModel=LogReadModel
)
logCrud = CrudForgery(
    crud_models=log_crud_models,
    session_manager= database_manager.session_manager
)
