from pydantic import BaseModel

class ThreatAnalysis(BaseModel):
    threat_name: str
    severity: str
    confidence: int
    recommendation: str