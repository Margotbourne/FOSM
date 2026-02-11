from lib.models.project import Project

class ProjectRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM project')
        projects = []
        for row in rows:
            item = Project(
                row["id"], row["name"], row["program_id"], 
                row["beneficiaries"], row["is_active"])
            projects.append(item)
        return projects

    def find_by_program(self, program_id):
        rows = self._connection.execute('SELECT * FROM project WHERE program_id = %s', [program_id])
        projects_in_program = []
        for row in rows:
            item = Project(row["id"], row["name"], row["program_id"], row["beneficiaries"], row["is_active"])
            projects_in_program.append(item)
        return projects_in_program

    def find(self, project_id):
        rows = self._connection.execute('SELECT * FROM project WHERE id = %s', [project_id])
        if not rows: return None 
        row = rows[0]
        return Project(row["id"], row["name"], row["program_id"], row["beneficiaries"], row["is_active"])
    
    def create(self, project):
        self._connection.execute(
            'INSERT INTO project (name, program_id, beneficiaries, is_active) VALUES (%s, %s, %s, %s)', 
            [project.name, project.program_id, project.beneficiaries, project.is_active]
        )
        return None

    def delete(self, project_id):
        self._connection.execute('DELETE FROM project WHERE id = %s', [project_id])
        return None