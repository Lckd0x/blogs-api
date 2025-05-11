from decimal import Decimal

class InvestmentStrategy:
    def __init__(self, monthly_investment: Decimal, extra_income: Decimal, return_rate: Decimal):
        self.monthly_investment = monthly_investment
        self.extra_income = extra_income
        self.monthly_rate = (Decimal(1) + return_rate) ** (Decimal(1)/Decimal(12)) - Decimal(1)
