from lib.models.supporter import Supporter
from lib.repositories.supporter_repository import SupporterRepository

def test_get_all_supporters(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = SupporterRepository(db_connection)
    assert len(repo.all()) == 2

def test_create_supporter(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = SupporterRepository(db_connection)
    repo.create(Supporter(None, "Charlie", "c@test.com", True, True, 100.00))
    assert len(repo.all()) == 3

def test_delete_supporter(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = SupporterRepository(db_connection)
    repo.delete(1)
    assert len(repo.all()) == 1