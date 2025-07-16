import random
import string

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from poetry_pytest_demo.db.model.base import TenantModel


@pytest.fixture
def test_session():

    TESTING_DB = "test_demo"
    test_conn_string_mysql = "mysql+mysqlconnector://root:root@localhost:3306/"

    def generate_random_string(length):
        """Generates a random string of a specified length."""
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choices(characters, k=length))
        return random_string

    # Generate a random 5-character string
    test_schema = generate_random_string(5)

    TEST_DB_NAME = f"{TESTING_DB}_{test_schema}"

    root_test_engine = create_engine(
        test_conn_string_mysql,
    )

    # MYSQL
    with root_test_engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {TEST_DB_NAME}"))

    test_engine = create_engine(
        test_conn_string_mysql + TEST_DB_NAME,  # use newly created test database
    )

    TenantModel.metadata.create_all(test_engine)

    Session = sessionmaker(bind=test_engine)
    test_session = Session()

    # Yield the session to the test
    yield test_session

    # Teardown code: Drop the test database after the test is done
    try:
        # Explicitly close the session before teardown
        test_session.close()
    except Exception as e:
        print(f"Error closing session: {e}")

    # Teardown code: Drop the test database after the test is done
    with root_test_engine.connect() as conn:
        conn.execute(text(f"DROP DATABASE IF EXISTS {TEST_DB_NAME}"))
