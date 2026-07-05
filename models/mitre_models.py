from pydantic import BaseModel

class MitreMapping(BaseModel):
    tactic: str
    technique_id: str
    technique_name: str
    explanation: str