from testproject.settings.auth.models import (
    Role,
    RolePrivilege,
    User,
    UserPrivilege,
    UserRole,
)

from testproject.settings.logger.model import LogModel
from testproject.task.models import Task
from testproject.settings.database import Base, database  # à importer en dernier

database.create_tables(target_metadata=Base.metadata)
