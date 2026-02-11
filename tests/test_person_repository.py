from lib.models.person import Person
from lib.repositories.person_repository import PersonRepository

def test_get_all_people(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = PersonRepository(db_connection)
    assert len(repo.all()) == 2

def test_create_person(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = PersonRepository(db_connection)
    repo.create(Person(None, "New Staff", "s@t.com", "Role", "Bio", "p.jpg"))
    assert len(repo.all()) == 3

def test_delete_person(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = PersonRepository(db_connection)
    repo.delete(1)
    assert len(repo.all()) == 1