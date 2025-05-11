from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from decimal import Decimal
from application.services import simulate_goal
from domain.exceptions  import InvalidInputError

router = APIRouter()

class GoalRequest(BaseModel):
    goal: Decimal
    time: int
    time_unit: str
    monthly_investment: Decimal
    extra_income: Decimal
    return_rate: Decimal
    start_date: str
    initial_value: Decimal = Decimal("0.00")
    one_time_investments: Dict[str, Decimal] = {}
    monthly_investment_changes: Dict[str, Decimal] = {}
    inflation_rate: Decimal = Decimal("0.00")

@router.post("/simulate")
def simulate(request: GoalRequest) -> Dict[str, Any]:
    try:
        results = simulate_goal(request)
        return {"data": results}
    except InvalidInputError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

