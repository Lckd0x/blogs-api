from  domain.exceptions  import InvalidInputError
class InvestmentPeriod:
    def __init__(self, time: int, unit: str):
        if time <= 0:
            raise InvalidInputError("Investment period must be greater than zero.")
        if unit not in ["months", "years"]:
            raise InvalidInputError("Invalid time unit. Use 'months' or 'years'.")

        self.months = time if unit == "months" else time * 12
