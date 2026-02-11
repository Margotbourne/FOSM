from lib.models.branch import Branch
from lib.repositories.branch_repository import BranchRepository

def test_get_all_branches(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = BranchRepository(db_connection)
    assert len(repo.all()) == 1

def test_create_branch(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = BranchRepository(db_connection)
    repo.create(Branch(None, "New Delhi", "DEL-01", "999", "St", "d@t.com", "INR"))
    assert len(repo.all()) == 2

def test_delete_branch(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = BranchRepository(db_connection)
    repo.delete(1)
    assert len(repo.all()) == 0