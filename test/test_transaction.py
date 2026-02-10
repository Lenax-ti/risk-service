# from src.models.transaction import Transaction, RiskCalculator, DecisionEngine
#
# def test_risk_calculator_simple():
#     # Создание объекта
#     t = Transaction(100000, 2, 'RU')
#
#     calculator = RiskCalculator()
#     score = calculator.calculate(t)
#
#     engine = DecisionEngine()
#     result = engine.decide(score)
#
#     assert result == 'SUSPICIOUS'
