from src.models.transaction import Transaction

class RiskCalculator:
    BASE_RISK = 1.0
    def calculate(self, transactions: Transaction) -> float:
        # self.transactions = transactions
        risk = self.BASE_RISK

        # Время
        if  18 < transactions.hour <= 22:
            risk -= 0.1
        elif transactions.hour > 22 or transactions.hour < 5:
            risk -= 0.2
        elif 5 <= transactions.hour <= 18:
            risk += 0.1
        # Регион
        if transactions.region != 'RU':
            risk -= 0.2

        # Сумма
        if 50_000 <= transactions.amount < 100_000:
            risk -= 0.2
        elif transactions.amount >= 100_000:
            risk -= 0.25

        return round(risk, 2)



