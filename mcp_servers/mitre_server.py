"""
MITRE MCP Server

This MCP server provides cybersecurity tools for querying
MITRE ATT&CK techniques.

Used by:
- MITRE Agent
- Coordinator Agent
"""

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------
# Create MCP Server
# ---------------------------------------------------

mcp = FastMCP("MITRE MCP Server")


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@mcp.tool()
def health_check() -> str:
    """
    Checks whether the MCP server is running.
    """
    return "MITRE MCP Server is running successfully."


# ---------------------------------------------------
# MITRE Lookup Tool
# ---------------------------------------------------

@mcp.tool()
def mitre_lookup(threat_name: str) -> dict:
    """
    Returns MITRE ATT&CK information
    based on the detected threat.
    """

    mitre_database = {

        "Brute Force Attack": {
            "technique_id": "T1110",
            "technique_name": "Brute Force",
            "tactic": "Credential Access"
        },

        "SQL Injection": {
            "technique_id": "T1190",
            "technique_name": "Exploit Public-Facing Application",
            "tactic": "Initial Access"
        },

        "Phishing": {
            "technique_id": "T1566",
            "technique_name": "Phishing",
            "tactic": "Initial Access"
        },

        "Ransomware": {
            "technique_id": "T1486",
            "technique_name": "Data Encrypted for Impact",
            "tactic": "Impact"
        }
    }

    return mitre_database.get(
        threat_name,
        {
            "technique_id": "Unknown",
            "technique_name": "Unknown",
            "tactic": "Unknown"
        }
    )


# ---------------------------------------------------
# Technique Details
# ---------------------------------------------------

@mcp.tool()
def technique_details(technique_id: str) -> str:
    """
    Returns additional information
    for a MITRE ATT&CK technique.
    """

    descriptions = {

        "T1110":
            "Brute Force involves repeated login attempts to guess credentials.",

        "T1190":
            "SQL Injection exploits vulnerable web applications.",

        "T1566":
            "Phishing tricks users into revealing credentials or executing malware.",

        "T1486":
            "Ransomware encrypts victim files to demand payment."
    }

    return descriptions.get(
        technique_id,
        "Technique not found."
    )


# ---------------------------------------------------
# Start Server
# ---------------------------------------------------

if __name__ == "__main__":
    mcp.run()