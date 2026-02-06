class Supporter:

    def __init__(self, id, name, email, is_gift_aid_eligible, marketing_consent, total_donated):
        self.id = id
        self.name = name 
        self.email = email
        self.is_gift_aid_eligible = is_gift_aid_eligible
        self.marketing_consent = marketing_consent
        self.total_donated = total_donated

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Supporter({self.id}, {self.name}, {self.email}, {self.is_gift_aid_eligible}, {self.marketing_consent}, {self.total_donated})"