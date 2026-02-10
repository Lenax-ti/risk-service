import pytest

from src.models.transaction import Transaction
from src.models.RiskCalculator import RiskCalculator

def test_risk_calculator():
    t = Transaction(120_000, 23, 'US')

    calculator = RiskCalculator()
    risk = calculator.calculate(t)
    assert risk == 0.35, f'Expected 0.35, got {risk}'
    # assert f'Expected 0.75, got {risk}'






