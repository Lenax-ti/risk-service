from src.models.transaction import Transaction
from src.models.RiskCalculator import RiskCalculator


t = Transaction(120000, 23, "US")
calculator = RiskCalculator()
risk = calculator.calculate(t)
print('Risk skore:',risk)
























