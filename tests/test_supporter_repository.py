from lib.models.supporter import Supporter
from lib.repositories.supporter_repository import SupporterRepository
from lib.repositories.donation_repository import DonationRepository

def test_get_all_supporters(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = SupporterRepository(db_connection)
    assert len(repo.all()) == 2

def test_create_supporter(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = SupporterRepository(db_connection)
    repo.create(Supporter(None, "Charlie", "c@test.com", True, True, 100.00))
    assert len(repo.all()) == 3

def test_delete_supporter(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    repo = SupporterRepository(db_connection)
    repo.delete(1)
    assert len(repo.all()) == 1



def test_delete_supporter_preserves_donations(db_connection):
    db_connection.seed("seeds/seva_mandir.sql")
    supporter_repo = SupporterRepository(db_connection)
    donation_repo = DonationRepository(db_connection)
    
    # 1. Alice has 2 donations
    assert len([d for d in donation_repo.all() if d.supporter_id == 1]) == 2
    
    # 2. Soft delete Alice
    supporter_repo.delete(1)
    
    # 3. VERIFY: The donations are STILL THERE (this is the preservation check)
    remaining_donations = [d for d in donation_repo.all() if d.supporter_id == 1]
    assert len(remaining_donations) == 2  # This now passes because we WANT to keep them!
    
    # 4. VERIFY: Alice is hidden from the active supporters list
    assert all(s.id != 1 for s in supporter_repo.all())