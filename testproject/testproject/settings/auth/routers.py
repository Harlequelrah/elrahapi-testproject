from profile.cruds import profile_crud

from elrahapi.relationship.many_to_many_class import ManyToManyClassRelationship
from elrahapi.relationship.one_to_many import OneToManyRelationship
from elrahapi.relationship.one_to_one import OneToOneRelationship
from elrahapi.router.router_provider import CustomRouterProvider
from elrahapi.router.router_routes_name import DefaultRoutesName
from task.cruds import task_crud

from .configs import authentication
from .cruds import (
    privilege_crud,
    role_crud,
    role_privilege_crud,
    user_crud,
    user_privilege_crud,
    user_role_crud,
)

user_role_relation = ManyToManyClassRelationship(
    relationship_name="user_roles",
    second_entity_crud=role_crud,
    relationship_crud=user_role_crud,
    relationship_key1_name="user_id",
    relationship_key2_name="role_id",
    default_public_relation_routes_name=ManyToManyClassRelationship.RELATION_RULES,
)
user_task_relation = OneToManyRelationship(
    relationship_name="user_tasks",
    second_entity_crud=task_crud,
    default_public_relation_routes_name=OneToManyRelationship.RELATION_RULES,
)
profile_relation = OneToOneRelationship(
    relationship_name="profile",
    second_entity_crud=profile_crud,
    default_public_relation_routes_name=OneToOneRelationship.RELATION_RULES,
)
user_router_provider = CustomRouterProvider(
    prefix="/users",
    tags=["users"],
    crud=user_crud,
    authentication=authentication,
    relations=[user_role_relation, user_task_relation, profile_relation],
)


user_privilege_router_provider = CustomRouterProvider(
    prefix="/users_privileges",
    tags=["user_privileges"],
    crud=user_privilege_crud,
    authentication=authentication,
)

role_router_provider = CustomRouterProvider(
    prefix="/roles",
    tags=["roles"],
    crud=role_crud,
    authentication=authentication,
)

privilege_router_provider = CustomRouterProvider(
    prefix="/privileges",
    tags=["privileges"],
    crud=privilege_crud,
    authentication=authentication,
)

role_privilege_router_provider = CustomRouterProvider(
    prefix="/roles_privileges",
    tags=["role_privileges"],
    crud=role_privilege_crud,
    authentication=authentication,
)

user_role_router_provider = CustomRouterProvider(
    prefix="/users_roles",
    tags=["user_roles"],
    crud=user_role_crud,
    authentication=authentication,
)


# user_router = user_router_provider.get_protected_router()
user_router = user_router_provider.get_mixed_router(
    public_routes_name=[
        DefaultRoutesName.CREATE,
    ],
    protected_routes_name=[
        DefaultRoutesName.READ_ONE,
        DefaultRoutesName.DELETE,
        DefaultRoutesName.UPDATE,
        DefaultRoutesName.PATCH,
        DefaultRoutesName.READ_ALL,
    ],
)

user_privilege_router = user_privilege_router_provider.get_protected_router()
user_role_router = user_role_router_provider.get_public_router()
role_router = role_router_provider.get_protected_router()
privilege_router = privilege_router_provider.get_protected_router()
role_privilege_router = role_privilege_router_provider.get_protected_router()
