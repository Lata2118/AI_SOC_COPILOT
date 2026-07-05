"""
Agent Skills
Defines the capabilities of each AI SOC Copilot agent.
"""

AGENT_SKILLS = {

    "Log Agent": [
        "Analyze uploaded security logs",
        "Identify suspicious IP addresses",
        "Count failed login attempts",
        "Summarize security events"
    ],

    "Threat Agent": [
        "Detect cyber attacks",
        "Classify attack type",
        "Estimate confidence score",
        "Recommend mitigation actions"
    ],

    "MITRE Agent": [
        "Map attacks to MITRE ATT&CK",
        "Identify tactic",
        "Identify technique",
        "Explain ATT&CK mapping"
    ],

    "Risk Agent": [
        "Calculate risk score",
        "Assign severity level",
        "Provide risk justification"
    ],

    "Report Agent": [
        "Generate executive summary",
        "Generate findings",
        "Generate recommendations",
        "Produce incident report"
    ]
}