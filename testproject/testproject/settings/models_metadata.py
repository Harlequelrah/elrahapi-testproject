from testproject.settings.logger.model import LogModel
from testproject.settings.auth.models import Role, RolePrivilege, User, UserRole
from testproject.settings.database import Base, database


# from testproject.task.models import Task

database.create_tables(target_metadata=Base.metadata)
