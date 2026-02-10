class Project:

    def __init__(self, id, name, program_id, beneficiaries, is_active) :
        self.id = id
        self.name = name 
        self.program_id = program_id
        self.benificaries = beneficiaries
        self.is_active = is_active
    
    def impact_statement(self):
        status = "currently active" if self.is_active else "completed"
        return f"The {self.name} project is {status}, reaching {self.benificaries} people"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Project({self.id}, '{self.name}', '{self.program_id}', '{self.benificaries}', '{self.is_active}')"