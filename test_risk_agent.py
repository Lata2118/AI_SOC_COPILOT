from agents.log_agent import analyze_logs
from agents.threat_agent import detect_threat
from agents.mitre_agent import map_mitre
from agents.risk_agent import assess_risk

logs = """
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Successful login from 192.168.1.20
"""

log_result = analyze_logs(logs)

threat = detect_threat(log_result)

mitre = map_mitre(threat)

risk = assess_risk(threat, mitre)

print(risk)

print()
print("Risk Score :", risk.risk_score)
print("Severity   :", risk.severity)
print("Reason     :", risk.justification)