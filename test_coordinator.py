from agents.coordinator_agent import investigate_incident

logs = """
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Successful login from 192.168.1.20
"""

result = investigate_incident(logs)

print("=" * 60)
print("AI SOC COPILOT")
print("=" * 60)

print("\nThreat")
print(result["threat"])

print("\nMITRE")
print(result["mitre"])

print("\nRisk")
print(result["risk"])

print("\nReport")
print(result["report"])