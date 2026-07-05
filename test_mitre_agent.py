from agents.log_agent import analyze_logs
from agents.threat_agent import detect_threat
from agents.mitre_agent import map_mitre

logs = """
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Successful login from 192.168.1.20
"""

log_result = analyze_logs(logs)

threat = detect_threat(log_result)

mitre = map_mitre(threat)

print(mitre)

print()
print("Tactic:", mitre.tactic)
print("Technique ID:", mitre.technique_id)
print("Technique Name:", mitre.technique_name)
print("Explanation:", mitre.explanation)