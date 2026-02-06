class Project:

    def __init__(self, id, name, program_id, beneficiaries, is_active) :
        self.id = id
        self.name = name 
        self.program_id = program_id
        self.benificaries = beneficiaries
        self.is_active = is_active

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Project({self.id}, {self.name}, {self.program_id}, {self.benificaries}, {self.is_active})"