class Person:

    def __init__(self, id, name, email, role, bio, image_url):
        self.id = id
        self.name = name 
        self.email = email
        self.role = role
        self.bio = bio
        self.image_url = image_url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Person({self.id}, {self.name}, {self.email}, {self.role}, {self.bio}, {self.image_url})"