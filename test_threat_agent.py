from agents.log_agent import analyze_logs
from agents.threat_agent import detect_threat

logs = """
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Successful login from 192.168.1.20
"""

log_result = analyze_logs(logs)

threat = detect_threat(log_result)

print(threat)
print()
print("Threat Name :", threat.threat_name)
print("Severity    :", threat.severity)
print("Confidence  :", threat.confidence)
print("Recommendation:")
print(threat.recommendation)