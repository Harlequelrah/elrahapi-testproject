from app.song.cruds import song_crud
from app.settings.config.auth_config import authentication
from elrahapi.router.router_namespace import DefaultRoutesName, TypeRoute
from elrahapi.router.router_provider import CustomRouterProvider

router_provider = CustomRouterProvider(
    prefix="/items",
    tags=["item"],
    crud=song_crud,
    # authentication=authentication,
)

song_router = router_provider.get_public_router()
# song_router = router_provider.get_protected_router()
