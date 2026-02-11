from lib.models.program import Program

"""
Program constructs
"""
def test_program_constructs():
    program = Program(1, "Test Name", "Test Description")
    assert program.id == 1
    assert program.name == "Test Name"
    assert program.description == "Test Description"
    assert program.projects == []


"""
We can format programs to strings nicely
"""
def test_programs_format_nicely():
    program = Program(1, "Test Name", "Test Description")

    assert str(program) == "Program(1, 'Test Name', 'Test Description', projects_count=0)"
    

"""
We can compare two identical programs
And have them be equal
"""
def test_programs_are_equal():
    program1 = Program(1, "Test Name", "Test Description")
    program2 = Program(1, "Test Name", "Test Description")
    assert program1 == program2