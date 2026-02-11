from lib.models.program import Program
from lib.repositories.program_repository import ProgramRepository

def test_get_all_programs(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)
    assert len(repo.all()) == 2

def test_find_program(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)
    program = repo.find(1)
    assert program.name == "Education"

def test_create_program(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)
    repo.create(Program(None, "Livelihoods", "Income projects"))
    assert len(repo.all()) == 3
    assert repo.all()[-1].name == "Livelihoods"

def test_delete_program(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)
    repo.create(Program(None, "Temp", "Delete Me"))
    new_id = repo.all()[-1].id
    repo.delete(new_id)
    assert len(repo.all()) == 2