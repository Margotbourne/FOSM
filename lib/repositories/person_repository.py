from lib.models.person import Person

class PersonRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM person')
        persons = [] 
        for row in rows:
            item = Person(
                row["id"], row["name"], row["email"], 
                row["role"], row["bio"], row["image_url"]
            )
            persons.append(item)
        return persons

    def find(self, person_id):
        rows = self._connection.execute('SELECT * FROM person WHERE id = %s', [person_id])
        if not rows: return None
        row = rows[0]
        return Person(row["id"], row["name"], row["email"], row["role"], row["bio"], row["image_url"])

    def create(self, person):
        self._connection.execute(
            'INSERT INTO person (name, email, role, bio, image_url) VALUES (%s, %s, %s, %s, %s)',
            [person.name, person.email, person.role, person.bio, person.image_url]
        )
        return None

    def delete(self, person_id):
        self._connection.execute('DELETE FROM person WHERE id = %s', [person_id])
        return None