from decimal import Decimal
from domain.exceptions import InvalidInputError

class InvestmentStrategy:
    def __init__(self, monthly_investment: Decimal, extra_income: Decimal, return_rate: Decimal):
        if monthly_investment < 0:
            raise InvalidInputError("Monthly investment cannot be negative.")
        if extra_income < 0:
            raise InvalidInputError("Extra income cannot be negative.")
        self.monthly_investment = monthly_investment
        self.extra_income = extra_income
        self.monthly_rate = (Decimal(1) + return_rate) ** (Decimal(1)/Decimal(12)) - Decimal(1)
