from poetry_pytest_demo.db.model.person import Person
from poetry_pytest_demo.db.session import db_session
from poetry_pytest_demo.queries.person import PersonQueries

new_person: Person = PersonQueries(db_session).create_person(name="Jane Doe", age=30)
