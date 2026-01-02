from elrahapi.authentication.authentication_manager import AuthenticationManager
from elrahapi.authentication.authentication_router_provider import (
    AuthenticationRouterProvider,
)
from testproject.settings.database import database_manager
from testproject.settings.secret import settings

from testproject.settings.auth.cruds import user_crud_models

user_crud_models.sqlalchemy_model.MAX_ATTEMPT_LOGIN = settings.user_max_attempt_login
authentication = AuthenticationManager(
    settings=settings,
    session_manager=database_manager.session_manager,
    authentication_models=user_crud_models,
)


authentication_router_provider = AuthenticationRouterProvider(
    authentication=authentication,
)
authentication_router = authentication_router_provider.get_auth_router()
