from sqlalchemy import (
    DECIMAL,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from testproject.settings.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    is_done = Column(Boolean, default=False)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)
    date_deleted = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="user_tasks")
    assigned_users = relationship(
        "User",
        secondary="task_assign_user_association",
        back_populates="assigned_tasks",
    )


task_assign_user_association = Table(
    "task_assign_user_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("task_id", Integer, ForeignKey("tasks.id"), nullable=False),
)
