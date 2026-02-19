from lib.models.user_authentication import compare_password_hash

class User:

    def __init__(self, id, name, email, password_hash, created_at=None):
        self.id = id
        self.name = name 
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at

    def check_password(self, password):
        return compare_password_hash(password, self.password_hash)
    

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email}, {self.password_hash}, {self.created_at})"