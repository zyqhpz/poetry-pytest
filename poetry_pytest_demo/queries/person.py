from sqlalchemy.orm import Session

from poetry_pytest_demo.db.model.person import Person


class PersonQueries:
    def __init__(self, session: Session):
        self.session = session

    def create_person(self, name: str, age: int) -> Person:
        new_person = Person(name=name, age=age)
        self.session.add(new_person)
        self.session.commit()
        return new_person

    def get_person_by_id(self, person_id: int) -> Person:
        return self.session.query(Person).filter(Person.id == person_id).first()
