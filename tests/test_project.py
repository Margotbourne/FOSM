from lib.models.project import Project

"""
Project constucts
"""
def test_project_constructs():
    project = Project(1, "Test Name", "Test Program_ID", "Test Benificaries", "Test Is_Active")
    assert project.id == 1
    assert project.name == "Test Name"
    assert project.program_id == "Test Program_ID"
    assert project.benificaries == "Test Benificaries"
    assert project.is_active == "Test Is_Active"


"""
Test impact statment 
"""
def test_impact_statemnt():
     project = Project(1, "Test Name", "Test Program_ID", "Test Benificaries", "Test Is_Active")
     assert project.impact_statement() == "The Test Name project is currently active, reaching Test Benificaries people"



"""
We can format projects to strings nicely
"""

def test_projects_format_nicely():
    project = Project(1, "Test Name", "Test Program_ID", "Test Benificaries", "Test Is_Active")
    assert str(project) == "Project(1, 'Test Name', 'Test Program_ID', 'Test Benificaries', 'Test Is_Active')"
    

"""
We can compare two identical projects
And have them be equal
"""
def test_projects_are_equal():
    project1 = Project(1, "Test Name", "Test Program_ID", "Test Benificaries", "Test Is_Active")
    project2 = Project(1, "Test Name", "Test Program_ID", "Test Benificaries", "Test Is_Active")
    assert project1 == project2
   