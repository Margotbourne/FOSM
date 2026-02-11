from lib.models.branch import Branch

class BranchRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM branch')
        branches = [] 
        for row in rows:
            item = Branch(
                row["id"], row["name"], row["region_code"], 
                row["charity_number"], row["address"], 
                row["email"], row["currency"]
            )
            branches.append(item)
        return branches

    def find(self, branch_id):
        rows = self._connection.execute('SELECT * FROM branch WHERE id = %s', [branch_id])
        if not rows: return None
        row = rows[0]
        return Branch(row["id"], row["name"], row["region_code"], row["charity_number"], row["address"], row["email"], row["currency"])

    def create(self, branch):
        self._connection.execute(
            'INSERT INTO branch (name, region_code, charity_number, address, email, currency) VALUES (%s, %s, %s, %s, %s, %s)',
            [branch.name, branch.region_code, branch.charity_number, branch.address, branch.email, branch.currency]
        )
        return None

    def delete(self, branch_id):
        self._connection.execute('DELETE FROM branch WHERE id = %s', [branch_id])
        return None