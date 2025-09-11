from elrahapi.relationship.many_to_many_table import ManyToManyTableRelationship
from elrahapi.relationship.many_to_one import ManyToOneRelationship
from elrahapi.router.router_namespace import DefaultRoutesName, TypeRoute
from elrahapi.router.router_provider import CustomRouterProvider
from settings.auth.configs import authentication
from settings.auth.cruds import user_crud
from task.cruds import task_crud
from task.models import task_assign_user_association

user_relation = ManyToOneRelationship(
    relationship_name="user",
    second_entity_crud=user_crud,
    default_public_relation_routes_name=ManyToOneRelationship.RELATION_RULES,
)
task_assign_user_relation = ManyToManyTableRelationship(
    relationship_name="assigned_users",
    second_entity_crud=user_crud,
    relation_table=task_assign_user_association,
    relationship_key1_name="task_id",
    relationship_key2_name="user_id",
    default_public_relation_routes_name=ManyToManyTableRelationship.RELATION_RULES,
)
router_provider = CustomRouterProvider(
    prefix="/tasks",
    tags=["task"],
    crud=task_crud,
    relations=[user_relation, task_assign_user_relation],
    # authentication=authentication,
    # roles=["ADMIN"],
    # privileges=["CAN_DO_SPECIAL_1"],
)

task_router = router_provider.get_public_router()
# app_myapp = router_provider.get_protected_router()
