from lib.models.supporter import Supporter

"""
Supporter constructs
"""
def test_supporter_constructs():
    supporter = Supporter(1, "Test Name", "Test Email", True, False, 150.50, True)
    assert supporter.id == 1
    assert supporter.name == "Test Name"
    assert supporter.email == "Test Email"
    assert supporter.is_gift_aid_eligible is True
    assert supporter.marketing_consent is False
    assert supporter.total_donated == 150.50
    assert supporter.is_active is True

"""
We can format supporters to strings nicely
"""
def test_supporter_format_nicely():
    supporter = Supporter(1, "Test Name", "Test Email", True, False, 150.50, True)
    
    assert str(supporter) == "Supporter(1, 'Test Name', 'Test Email', True, False, 150.5, True)"

"""
We can compare two identical supporters
And have them be equal
"""
def test_supporter_are_equal():
    supporter1 = Supporter(1, "Test Name", "Test Email", True, False, 150.50, True)
    supporter2 = Supporter(1, "Test Name", "Test Email", True, False, 150.50, True)
    assert supporter1 == supporter2
