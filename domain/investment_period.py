class InvestmentPeriod:
    def __init__(self, time: int, unit: str):
        self.months = time if unit == "months" else time * 12
