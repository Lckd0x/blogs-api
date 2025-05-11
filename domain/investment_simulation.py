from decimal import Decimal, ROUND_HALF_UP
from typing import Dict
from datetime import datetime
from dateutil.relativedelta import relativedelta

class InvestmentSimulation:
    def __init__(self, goal, strategy, period, initial_value: Decimal):
        self.goal = goal
        self.strategy = strategy
        self.period = period
        self.initial_value = initial_value
        self.results = {}

    def run(self, one_time_investments: Dict[str, Decimal], monthly_investment_changes: Dict[str, Decimal]) -> Dict[str, Dict]:
        value, value_with_extra = self.initial_value, self.initial_value
        current_investment = self.strategy.monthly_investment

        for i in range(self.period.months):
            date = self.goal.start_date + relativedelta(months=i)
            key = date.strftime("%m-%Y")

            if key in monthly_investment_changes:
                current_investment = monthly_investment_changes[key]

            punctual = one_time_investments.get(key, Decimal("0.00"))

            value = value * (Decimal(1) + self.strategy.monthly_rate) + current_investment + punctual
            value_with_extra = value_with_extra * (Decimal(1) + self.strategy.monthly_rate) + self.strategy.extra_income + punctual

            adjusted_goal = self.goal.adjust_goal(i)

            self.results[key] = {
                "current_value": float(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
                "current_extra_value": float(value_with_extra.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
                "adjusted_goal_value": float(adjusted_goal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),  # NEW FIELD
                "goal_achieved": "Y" if value + value_with_extra >= adjusted_goal else "N"
            }

        return self.results
