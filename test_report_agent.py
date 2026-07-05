from agents.log_agent import analyze_logs
from agents.threat_agent import detect_threat
from agents.mitre_agent import map_mitre
from agents.risk_agent import assess_risk
from agents.report_agent import generate_report

logs = """
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Successful login from 192.168.1.20
"""

log = analyze_logs(logs)
threat = detect_threat(log)
mitre = map_mitre(threat)
risk = assess_risk(threat, mitre)

report = generate_report(log, threat, mitre, risk)

print(report)