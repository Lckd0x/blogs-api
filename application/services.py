from domain.financial_goal import FinancialGoal
from domain.investment_strategy import InvestmentStrategy
from domain.investment_period import InvestmentPeriod
from domain.investment_simulation import InvestmentSimulation

def simulate_goal(goal_data):
    goal = FinancialGoal(goal_data.goal, goal_data.start_date, goal_data.inflation_rate)
    strategy = InvestmentStrategy(goal_data.monthly_investment, goal_data.extra_income, goal_data.return_rate)
    period = InvestmentPeriod(goal_data.time, goal_data.time_unit)

    simulation = InvestmentSimulation(goal, strategy, period, goal_data.initial_value)
    results = simulation.run(goal_data.one_time_investments, goal_data.monthly_investment_changes)

    return results
