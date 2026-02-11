from lib.models.program import Program
from lib.models.project import Project

class ProgramRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM program')
        programs = [] 
        for row in rows:
            item = Program(
                row["id"], row["name"], row["description"]
            )
            programs.append(item)
        return programs

    def find(self, program_id):
        rows = self._connection.execute('SELECT * FROM program WHERE id = %s', [program_id])
        if not rows: return None
        row = rows[0]
        return Program(row["id"], row["name"], row["description"])
    
    def find_with_projects(self, program_id):
        program = self.find(program_id)
        if not program: return None
        rows = self._connection.execute(
        "SELECT * FROM project WHERE program_id = %s", [program_id]
    )

        program.projects = []
        for row in rows:
            project = Project(
                row["id"], row["name"], row["program_id"], 
                row["beneficiaries"], row["is_active"]
            )
            program.projects.append(project)
        
        return program
    
    def create(self, program):
        self._connection.execute(
            'INSERT INTO program (name, description) VALUES (%s, %s)',
            [program.name, program.description]
        )
        return None

    def delete(self, program_id):
        self._connection.execute('DELETE FROM program WHERE id = %s', [program_id])
        return None