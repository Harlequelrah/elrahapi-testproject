from elrahapi.middleware.models import MetaLogModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from testproject.settings.database import Base


class LogModel(Base, MetaLogModel):
    __tablename__ = "logs"
    USER_FK_NAME = "user_id"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="user_logs")


# vous pouvez adapter  la classe selon vos besoin
