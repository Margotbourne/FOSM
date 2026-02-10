from lib.models.supporter import Supporter

"""
Supporter constucts
"""
def test_supporters_constructs():
    supporter = Supporter(1, "Test Name", "Test Email", "Test Is_gift_aid_eligible", "Test Marketing_consent", "Test Total_donated")
    assert supporter.id == 1
    assert supporter.name == "Test Name"
    assert supporter.email == "Test Email"
    assert supporter.is_gift_aid_eligible == "Test Is_gift_aid_eligible"
    assert supporter.marketing_consent == "Test Marketing_consent"
    assert supporter.total_donated == "Test Total_donated"

def test_supporters_constructs():
    # id (int), name (str), email (str), gift_aid (bool), marketing (bool), total (float)
    supporter = Supporter(1, "Test Name", "test@email.com", True, False, 150.50)
    
    assert supporter.is_gift_aid_eligible is True  # Real boolean check
    assert supporter.total_donated == 150.50       # Real number check

"""
We can format supporters to strings nicely
"""
def test_supporters_format_nicely():
    supporter = Supporter(1, "Test Name", "Test Email", "Test Is_gift_aid_eligible", "Test Marketing_consent", "Test Total_donated")
    assert str(supporter) == "Supporter(1, 'Test Name', 'Test Email', Test Is_gift_aid_eligible, Test Marketing_consent, Test Total_donated)"
    

"""
We can compare two identical supporters
And have them be equal
"""
def test_supporters_are_equal():
    supporter1 = Supporter(1, "Test Name", "Test Email", "Test Is_gift_aid_eligible", "Test Marketing_consent", "Test Total_donated")
    supporter2 = Supporter(1, "Test Name", "Test Email", "Test Is_gift_aid_eligible", "Test Marketing_consent", "Test Total_donated")
    assert supporter1 == supporter2
   