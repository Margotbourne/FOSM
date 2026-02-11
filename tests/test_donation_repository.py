from lib.models.donation import Donation
from lib.repositories.donation_repository import DonationRepository
from lib.repositories.supporter_repository import SupporterRepository

"""
When we call #all, we get all donation records
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    supp_repo = SupporterRepository(db_connection)
    repo = DonationRepository(db_connection, supp_repo)

    donations = repo.all()
    assert len(donations) == 2
    assert float(donations[0].amount) == 500.00 
    assert float(donations[1].amount) == 700.00

"""
When we call #create, we see a new record AND the supporter total updates
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    supp_repo = SupporterRepository(db_connection)
    don_repo = DonationRepository(db_connection, supp_repo)

    don_repo.create(Donation(None, 2, 150.00, "2026-03-01"))

    donations = don_repo.all()
    assert len(donations) == 3
    
    # Verify the sync worked on Supporter 2
    bob = supp_repo.find(2)
    # If Bob started at 0, he should now be at 150.00
    assert float(bob.total_donated) == 150.00

"""
When we create a donation, the supporter's total_donated 
column should update automatically.
"""
def test_donation_creation_updates_supporter_total(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    supp_repo = SupporterRepository(db_connection)
    don_repo = DonationRepository(db_connection, supp_repo)

    # 1. Arrange: Alice (ID 1) starts with 1200.00
    alice = supp_repo.find(1)
    assert float(alice.total_donated) == 1200.0

    # 2. Act: Add a new donation of 100.00
    new_donation = Donation(None, 1, 100.0, "2026-02-11")
    don_repo.create(new_donation)

    # 3. Assert: Supporter table is refreshed
    alice_updated = supp_repo.find(1)
    assert float(alice_updated.total_donated) == 1300.0

"""
We can find all donations specifically for one supporter
"""
def test_find_by_supporter(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    supp_repo = SupporterRepository(db_connection)
    don_repo = DonationRepository(db_connection, supp_repo)

    alice_donations = don_repo.find_by_supporter(1)
    assert len(alice_donations) == 2
    assert float(alice_donations[0].amount) == 500.0
    assert float(alice_donations[1].amount) == 700.0
