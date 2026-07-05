from pydantic import BaseModel

class LogAnalysis(BaseModel):
    suspicious_ips: list[str]
    failed_login_count: int
    attack_type: str
    summary: str