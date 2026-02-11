from lib.models.donation import Donation
from lib.repositories.donation_repository import DonationRepository

"""
When we call #all, we get all donation records
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = DonationRepository(db_connection)

    donations = repo.all()

    assert len(donations) == 2
    assert donations[0].amount == 500.00
    assert donations[1].amount == 700.00
    assert donations[0].supporter_id == 1

"""
When we call #find, we get a single donation record by ID
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = DonationRepository(db_connection)

    donation = repo.find(1)
    assert donation.amount == 500.00
    assert donation.supporter_id == 1

"""
When we call #create, we see a new record in the list
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = DonationRepository(db_connection)

    repo.create(Donation(None, 2, 150.00, "2024-03-01"))

    donations = repo.all()
    assert len(donations) == 3
    assert donations[-1].amount == 150.00
    assert donations[-1].supporter_id == 2

"""
When we call #delete, we remove the record from the list
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = DonationRepository(db_connection)

    repo.delete(1) # Remove Alice's first donation

    donations = repo.all()
    assert len(donations) == 1
    assert donations[0].amount == 700.00