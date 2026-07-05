from agents.log_agent import analyze_logs

logs = """
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Failed login from 192.168.1.10
Successful login from 192.168.1.20
"""

result = analyze_logs(logs)

print(result)
print(result.suspicious_ips)
print(result.attack_type)
print(result.failed_login_count)
print(result.summary)