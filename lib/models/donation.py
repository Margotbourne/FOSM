class Donation:
    def __init__(self, id, supporter_id, amount, donation_date):
        self.id = id
        self.supporter_id = supporter_id
        self.amount = amount
        self.donation_date = donation_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Donation({self.id}, {self.supporter_id}, {self.amount}, {self.donation_date})"