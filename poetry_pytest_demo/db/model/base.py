from sqlalchemy.orm import declarative_base


class BaseModel:
    __abstract__ = True

    @classmethod
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.__tablename__ = cls.__name__.lower()


global TenantModel
TenantModel = declarative_base(cls=BaseModel)
