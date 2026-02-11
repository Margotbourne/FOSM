from lib.models.program import Program
from lib.repositories.program_repository import ProgramRepository

def test_get_all_programs(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)
    
    programs = repo.all()
    assert len(programs) == 2
    assert programs[0] == Program(1, 'Education', 'Rural education programs for tribal children.')

def test_find_program(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)
    
    program = repo.find(2)
    assert program == Program(2, 'Health', 'Primary healthcare and nutrition services.')

def test_create_program(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)
    
    new_program = Program(None, "Livelihoods", "Helping farmers improve crop yields.")
    repo.create(new_program)
    
    programs = repo.all()
    assert len(programs) == 3
    assert programs[-1].name == "Livelihoods"

def test_delete_program(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProgramRepository(db_connection)

    repo.delete(2)
    all_programs = repo.all()
    assert len(all_programs) == 1
    assert repo.find(2) is None