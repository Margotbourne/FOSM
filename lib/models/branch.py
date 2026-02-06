class Branch:
    
    def __init__(self, id, name, region_code, charity_number, address, email, curreency):
        self.id = id
        self.name = name
        self.region_code = region_code
        self.charity_number = charity_number
        self.address = address
        self.email = email
        self.currency = curreency

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Branch({self.id}, {self.name}, {self.region_code}, {self.charity_number}, {self.address}, {self.email}, {self.currency})"
