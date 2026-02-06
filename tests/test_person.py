from lib.models.person import Person

"""
Person constucts
"""
def test_persons_constructs():
    person = Person(1, "Test Name", "Test Email", "Test Role", "Test Bio", "Test Image_url")
    assert person.id == 1
    assert person.name == "Test Name"
    assert person.email == "Test Email"
    assert person.role == "Test Role"
    assert person.bio == "Test Bio"
    assert person.image_url == "Test Image_url"


"""
We can format persons to strings nicely
"""
def test_persons_format_nicely():
    person = Person(1, "Test Name", "Test Email", "Test Role", "Test Bio", "Test Image_url")
    assert str(person) == "Person(1, Test Name, Test Email, Test Role, Test Bio, Test Image_url)"
    

"""
We can compare two identical people
And have them be equal
"""
def test_persons_are_equal():
    person1 = Person(1, "Test Name", "Test Email", "Test Role", "Test Bio", "Test Image_url")
    person2 = Person(1, "Test Name", "Test Email", "Test Role", "Test Bio", "Test Image_url")
    assert person1 == person2
   