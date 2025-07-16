from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from poetry_pytest_demo.db.model.base import TenantModel

STAGING_DB = "demo"

conn_string_mysql = "mysql+mysqlconnector://mysql:root@localhost:3306/" + STAGING_DB

engine = create_engine(
    conn_string_mysql,
    echo=True,  # Optional: shows SQL in console
)
TenantModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db_session = Session()
