from lib.models.donation import Donation

class DonationRepository:
    def __init__(self, connection, supporter_repo):
        self._connection = connection
        self._supporter_repo = supporter_repo

    def all(self):
        rows = self._connection.execute('SELECT * FROM donations ORDER BY donation_date DESC')
        return [
            Donation(row["id"], row["supporter_id"], row["amount"], row["donation_date"])
            for row in rows
        ]

    
    def find_by_supporter(self, supporter_id):
        rows = self._connection.execute(
            'SELECT * FROM donations WHERE supporter_id = %s ORDER BY donation_date DESC',
            [supporter_id]
        )
        return [
            Donation(row["id"], row["supporter_id"], row["amount"], row["donation_date"])
            for row in rows
        ]

    # 3. Create a donation AND update the supporter's total (The "Sync" logic)
    def create(self, donation):
        # Save the donation record
        self._connection.execute(
            'INSERT INTO donations (amount, donation_date, supporter_id) VALUES (%s, %s, %s)',
            [donation.amount, donation.donation_date, donation.supporter_id]
        )
        
        # Immediately refresh the supporter's "Total Donated" column
        self._supporter_repo.update_total_donated(donation.supporter_id)
        return None

