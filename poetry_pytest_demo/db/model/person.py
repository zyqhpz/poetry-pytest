from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from poetry_pytest_demo.db.model.base import TenantModel


class Person(TenantModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
