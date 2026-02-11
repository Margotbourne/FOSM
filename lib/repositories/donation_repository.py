from lib.models.donation import Donation

class DonationRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM donations')
        donations = [] 
        for row in rows:
            item = Donation(
                row["id"], row["supporter_id"], row["amount"], 
                row["donation_date"]
            )
            donations.append(item)
        return donations

    def find(self, donation_id):
        rows = self._connection.execute('SELECT * FROM donations WHERE id = %s', [donation_id])
        if not rows: return None
        row = rows[0]
        return Donation(row["id"], row["supporter_id"], row["amount"], row["donation_date"])

    def create(self, donation):
        rows = self._connection.execute(
            'INSERT INTO donations (supporter_id, amount, donation_date) '
            'VALUES (%s, %s, %s) RETURNING id', # <--- Add RETURNING id
            [donation.supporter_id, donation.amount, donation.donation_date]
        )
        row = rows[0]
        donation.id = row["id"] # <--- Update the object with the new ID
        return donation

    def delete(self, donation_id):
        self._connection.execute('DELETE FROM donations WHERE id = %s', [donation_id])
        return None