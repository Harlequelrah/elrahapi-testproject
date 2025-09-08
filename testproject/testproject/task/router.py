from elrahapi.router.router_namespace import DefaultRoutesName, TypeRoute
from elrahapi.router.router_provider import CustomRouterProvider
from settings.auth.configs import authentication
from task.cruds import task_crud

router_provider = CustomRouterProvider(
    prefix="/tasks",
    tags=["task"],
    crud=task_crud,
    authentication=authentication,
    # roles=["ADMIN"],
    privileges=["CAN_DO_SPECIAL_1"],
)

task_router = router_provider.get_protected_router()
# app_myapp = router_provider.get_protected_router()
