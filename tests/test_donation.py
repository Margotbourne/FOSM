from lib.models.donation import Donation

"""
Donation constructs
"""
def test_donation_constructs():
    donation = Donation(1, "Test Supporter_ID", "Test Amount", "Test Donation_Date")
    assert donation.id == 1
    assert donation.supporter_id == "Test Supporter_ID"
    assert donation.amount == "Test Amount"
    assert donation.donation_date == "Test Donation_Date"



"""
We can format donations to strings nicely
"""
def test_donations_format_nicely():
    donation = Donation(1, "Test Supporter_ID", "Test Amount", "Test Donation_Date")
    assert str(donation) == "Donation(1, Test Supporter_ID, Test Amount, Test Donation_Date)"
    

"""
We can compare two identical doantions
And have them be equal
"""
def test_donations_are_equal():
    donation1 = Donation(1, "Test Supporter_ID", "Test Amount", "Test Donation_Date")
    donation2 = Donation(1, "Test Supporter_ID", "Test Amount", "Test Donation_Date")
    assert donation1 == donation2