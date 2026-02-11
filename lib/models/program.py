class Program:
    def __init__(self, id, name, description, projects = None):
        self.id = id
        self.name = name
        self.description = description
        self.projects = projects if projects is not None else []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Program({self.id}, '{self.name}', '{self.description}', projects_count={len(self.projects)})"