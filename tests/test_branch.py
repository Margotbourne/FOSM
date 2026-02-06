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
def test_branches_are_equal():
    branch1 = Branch(1, "Test Name", "Test Region-Code", "Test Charity-Number", "Test Address", "Test Email", "Test Currency")
    branch2 = Branch(1, "Test Name", "Test Region-Code", "Test Charity-Number", "Test Address", "Test Email", "Test Currency")
    assert branch1 == branch2
   