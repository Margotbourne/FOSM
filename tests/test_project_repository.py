from lib.models.project import Project
from lib.repositories.project_repository import ProjectRepository

def test_get_all_projects(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProjectRepository(db_connection)
    assert len(repo.all()) == 3

def test_find_projects_by_program(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProjectRepository(db_connection)
    # Testing that education (ID 1) has 2 projects
    edu_projects = repo.find_by_program(1)
    assert len(edu_projects) == 2

def test_create_project(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProjectRepository(db_connection)
    repo.create(Project(None, "New Well", 2, 50, True))
    assert len(repo.all()) == 4
    assert repo.all()[-1].name == "New Well"

def test_delete_project(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = ProjectRepository(db_connection)
    repo.delete(1)
    assert len(repo.all()) == 2
    assert repo.find(1) is None