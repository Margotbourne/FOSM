from lib.models.branch import Branch

"""
Branch constucts with id, name, region_code, charity_number, address, email, currency.
"""
def test_branch_constructs():
    branch = Branch(1, "Test Name", "Test Region-Code", "Test Charity-Number", "Test Address", "Test Email", "Test Currency")
    assert branch.id == 1
    assert branch.name == "Test Name"
    assert branch.region_code == "Test Region-Code"
    assert branch.charity_number == "Test Charity-Number"
    assert branch.address == "Test Address"
    assert branch.email == "Test Email"
    assert branch.currency == "Test Currency"


"""
We can format branches to strings nicely
"""
def test_braches_format_nicely():
    branch = Branch(1, "Test Name", "Test Region-Code", "Test Charity-Number", "Test Address", "Test Email", "Test Currency")
    assert str(branch) == "Branch(1, Test Name, Test Region-Code, Test Charity-Number, Test Address, Test Email, Test Currency)"
    

"""
We can compare two identical branches
And have them be equal
"""
def test_braches_format_nicely():
    branch = Branch(1, "Test Name", "Test Region-Code", "Test Charity-Number", "Test Address", "Test Email", "Test Currency")
    assert str(branch) ==  "Branch(id=1, name='Test Name', region='Test Region-Code', charity_no='Test Charity-Number', currency='Test Currency')"

"""
Test two branches are not equal 
"""
   
def test_branches_are_not_equal():
    branch1 = Branch(1, "Test Name", "Test Region-Code", "Test Charity-Number", "Test Address", "Test Email", "Test Currency")
    branch2 = Branch(2, "Test Name2", "Test Region-Code2", "Test Charity-Number2", "Test Address2", "Test Email2", "Test Currency2")
    assert branch1 != branch2