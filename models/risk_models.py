from pydantic import BaseModel

class RiskAssessment(BaseModel):
    risk_score: int
    severity: str
    justification: str