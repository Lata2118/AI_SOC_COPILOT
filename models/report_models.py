from pydantic import BaseModel

class IncidentReport(BaseModel):
    incident_title: str
    executive_summary: str
    findings: str
    mitre_mapping: str
    risk_assessment: str
    recommendations: str