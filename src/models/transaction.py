class Transaction:
    def __init__(self, amount, hour, region):
        self.amount = amount
        self.hour = hour
        self.region = region

    def to_dict(self):
        return {'amount': self.amount,
                'hour': self.hour,
                'region': self.region}


class RiskCalculator:
    def calculate(self, transactions: Transaction) -> float:
        # self.transactions = transactions
        risk_score = 1.0
        if  18 < transactions.hour < 22:
            risk_score -= 0.1
        elif 22 < transactions.hour:
            risk_score -= 0.2

        if transactions.region != 'RU':
            risk_score -= 0.2

        if 50000 <= transactions.amount < 100000:
            risk_score -= 0.2
        elif transactions.amount >= 100000:
            risk_score -= 0.25

        return risk_score

class DecisionEngine:
    def decide(self, risk_score: float) -> str:
        if risk_score > 0.8:
            return 'OK'
        elif risk_score >= 0.5:
            return 'SUSPICIOUS'
        else:
            return 'BLOCKED'




# t = Transaction(100000, 2, "RU")
#
# calculator = RiskCalculator()
# score = calculator.calculate(t)
#
# engine = DecisionEngine()
# result = engine.decide(score)
#
# print(result)
# print(calculator.calculate(t))
