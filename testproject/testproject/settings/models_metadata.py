from testproject.settings.database import database
from testproject.settings.auth.models import User, Role, UserRole, RolePrivilege
from testproject.settings.logger.model import LogModel, Base

database.create_tables(target_metadata=Base.metadata)
