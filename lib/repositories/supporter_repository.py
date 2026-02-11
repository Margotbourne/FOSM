from lib.models.supporter import Supporter

class SupporterRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM supporter')
        supporters = []
        for row in rows:
            item = Supporter(
                row["id"], row["name"], row["email"], 
                row["is_gift_aid_eligible"], row["marketing_consent"], 
                row["total_donated"]
            )
            supporters.append(item)
        return supporters

    def find(self, supporter_id):
        rows = self._connection.execute('SELECT * FROM supporter WHERE id = %s', [supporter_id])
        if not rows: return None
        row = rows[0]
        return Supporter(
            row["id"], row["name"], row["email"], 
            row["is_gift_aid_eligible"], row["marketing_consent"], 
            row["total_donated"]
        )

    def create(self, supporter):
        self._connection.execute(
            'INSERT INTO supporter (name, email, is_gift_aid_eligible, marketing_consent, total_donated) VALUES (%s, %s, %s, %s, %s)',
            [
                supporter.name, supporter.email, 
                supporter.is_gift_aid_eligible, supporter.marketing_consent, 
                supporter.total_donated
            ]
        )
        return None

    def delete(self, supporter_id):
        self._connection.execute('DELETE FROM supporter WHERE id = %s', [supporter_id])
        return None