from testproject.settings.logger.model import LogModel
from testproject.settings.auth.models import (
    Role,
    RolePrivilege,
    User,
    UserPrivilege,
    UserRole,
)
from testproject.settings.database import Base, database_manager  # à importer en dernier


database_manager.create_tables(target_metadata=Base.metadata)
