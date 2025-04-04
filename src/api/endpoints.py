from fastapi import APIRouter
from src.core.analytics import revenue_trend, cancellation_rate, geographical_distribution, lead_time_distribution
from src.core.rag_model import ask_question
from pydantic import BaseModel

router = APIRouter()

@router.get("/analytics")
def get_analytics(metric: str):
    analytics_map = {
        "revenue_trend": revenue_trend,
        "cancellation_rate": cancellation_rate,
        "geographical_distribution": geographical_distribution,
        "lead_time_distribution": lead_time_distribution
    }
    if metric in analytics_map:
        return analytics_map[metric]()
    return {"error": "Invalid metric"}

# Define request body model
class AskRequest(BaseModel):
    query: str

@router.post("/ask")
def ask_query(request: AskRequest):
    return {"response": ask_question(request.query)}