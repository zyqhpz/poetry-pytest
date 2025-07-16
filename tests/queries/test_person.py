from poetry_pytest_demo.db.model.person import Person
from poetry_pytest_demo.queries.person import PersonQueries


def test_create_person(test_session):
    """Test creating a person."""

    # Create a new person
    person_name = "John Doe"
    person_age = 25
    new_person = PersonQueries(test_session).create_person(
        name=person_name, age=person_age
    )

    # Verify the person was created
    assert new_person.name == person_name
    assert new_person.age == person_age


def test_get_person(test_session):
    """Test retrieving a person."""

    new_person = Person(name="Jane Doe", age=30)

    test_session.add(new_person)
    test_session.commit()

    # Retrieve the person by ID
    retrieved_person = PersonQueries(test_session).get_person_by_id(new_person.id)

    # Verify the retrieved person's details
    assert retrieved_person.id == new_person.id
    assert retrieved_person.name == new_person.name
    assert retrieved_person.age == new_person.age
