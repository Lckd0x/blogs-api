from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
from dateutil.relativedelta import relativedelta
from  domain.exceptions  import InvalidInputError

class FinancialGoal:
    def __init__(self, goal: Decimal, start_date: str, inflation_rate: Decimal = Decimal("0.00")):
        if goal <= 0:
            raise InvalidInputError("Goal amount must be greater than zero.")
        try:
            self.start_date = datetime.strptime(start_date, "%m-%Y")
        except ValueError:
            raise InvalidInputError("Invalid start date format. Use 'MM-YYYY'.")
        self.goal = goal
        self.start_date = datetime.strptime(start_date, "%m-%Y")
        self.inflation_rate = inflation_rate

    def adjust_goal(self, months: int) -> Decimal:
        monthly_inflation = (Decimal(1) + self.inflation_rate) ** (Decimal(1)/Decimal(12)) - Decimal(1)
        adjusted_goal = self.goal
        for _ in range(months):
            adjusted_goal *= (Decimal(1) + monthly_inflation)
        return adjusted_goal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
