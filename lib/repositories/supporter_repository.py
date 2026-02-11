from lib.models.supporter import Supporter

class SupporterRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM supporter WHERE is_active = TRUE')
        supporters = []
        for row in rows:
            item = Supporter(
                row["id"], row["name"], row["email"], 
                row["is_gift_aid_eligible"], row["marketing_consent"], 
                row["total_donated"], row["is_active"]
            )
            supporters.append(item)
        return supporters

    def find(self, supporter_id):
        rows = self._connection.execute(
            'SELECT * FROM supporter WHERE id = %s AND is_active = TRUE', 
            [supporter_id]
        )
        if not rows: return None
        row = rows[0]
        return Supporter(
            row["id"], row["name"], row["email"], 
            row["is_gift_aid_eligible"], row["marketing_consent"], 
            row["total_donated"], row["is_active"]
        )

    def create(self, supporter):
        self._connection.execute(
            'INSERT INTO supporter (name, email, is_gift_aid_eligible, marketing_consent, total_donated, is_active) VALUES (%s, %s, %s, %s, %s, %s)',
            [
                supporter.name, supporter.email, 
                supporter.is_gift_aid_eligible, supporter.marketing_consent, 
                supporter.total_donated,
                supporter.is_active
            ]
        )
        return None

    def delete(self, supporter_id):
        # Change DELETE to UPDATE to preserve the record
        self._connection.execute(
            'UPDATE supporter SET is_active = FALSE WHERE id = %s', 
            [supporter_id]
        )
        return None
    

    def update_total_donated(self, supporter_id):
        query = "SELECT SUM(amount) AS total FROM donations WHERE supporter_id = %s"
        result = self._connection.execute(query, [supporter_id])
        new_total = result[0]["total"] or 0

        self._connection.execute(
            "UPDATE supporter SET total_donated = %s WHERE id = %s",
            [new_total, supporter_id]
    )