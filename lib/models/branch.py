class Branch:
    def __init__(self, id, name, region_code, charity_number, address, email, currency="GBP"):
        self.id = id
        self.name = name
        self.region_code = region_code
        self.charity_number = charity_number
        self.address = address
        self.email = email
        self.currency = currency # Fixed typo

    def __eq__(self, other):
        if not isinstance(other, Branch):
            return False
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return (f"Branch(id={self.id}, name='{self.name}', region='{self.region_code}', "
                f"charity_no='{self.charity_number}', currency='{self.currency}')")
