class Transaction:
    def __init__(self, amount, hour, region):
        self.amount = amount
        self.hour = hour
        self.region = region

    def is_night(self):
        return self.hour < 6

    def to_dict(self):
        return {'amount': self.amount,
                'hour': self.hour,
                'region': self.region}



