from elrahapi.router.router_namespace import (
    DefaultRoutesName,
    TypeRoute,
)
from elrahapi.router.router_provider import CustomRouterProvider

from testproject.settings.auth.configs import authentication
from testproject.testapp3.cruds import testapp3_crud

router_provider = CustomRouterProvider(
    prefix="/items",
    tags=["item"],
    crud=testapp3_crud,
    # authentication=authentication,
)

testapp3_router = router_provider.get_public_router()
# testapp3_router = router_provider.get_protected_router()

