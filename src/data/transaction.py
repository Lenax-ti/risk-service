class Transaction:
    ANTI_FRAUND = 1
    def __init__(self, amount, hour, region):
        self.amount = amount
        self.hour = hour
        self.region = region
        self.check_transaction()



    def is_night(self):
            if 18 < self.hour < 22:
                self.ANTI_FRAUND -= 0.1
            elif 22 < self.hour < 5:
                self.ANTI_FRAUND += 0.2

    def is_region(self):
        if self.region != 'RU':
            self.ANTI_FRAUND -= 0.2

    def quantity(self):
        if 50000 <= self.amount < 100000:
            self.ANTI_FRAUND -= 0.2
        if self.amount >= 100000:
            self.ANTI_FRAUND -= 0.25

    def check_transaction(self):
        self.is_night()
        self.is_region()
        self.quantity()
        if 0.8 <= self.ANTI_FRAUND:
            return print('Все в порядке')
        elif 0.51 <= self.ANTI_FRAUND <= 0.79:
            return print('Подозрительная операция, подтвердите личность')
        elif 0.5 > self.ANTI_FRAUND:
            return print('Карта заблокирована. Обратитесь в банк')

    def to_dict(self):
        return {'amount': self.amount,
                'hour': self.hour,
                'region': self.region}

t2 = Transaction(500000, 6, 'US')

