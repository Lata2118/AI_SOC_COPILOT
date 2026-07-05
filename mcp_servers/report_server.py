"""
Report & Risk MCP Server

Provides risk calculation and report generation tools.

Used by:
- Risk Agent
- Report Agent
"""

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------
# Create MCP Server
# ---------------------------------------------------

mcp = FastMCP("Report & Risk MCP Server")


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@mcp.tool()
def health_check() -> str:
    """
    Checks whether the MCP server is running.
    """
    return "Report & Risk MCP Server is running successfully."


# ---------------------------------------------------
# Risk Calculation
# ---------------------------------------------------

@mcp.tool()
def calculate_risk(severity: str) -> dict:
    """
    Returns a risk score based on severity.
    """

    severity = severity.lower()

    mapping = {
        "critical": 95,
        "high": 80,
        "medium": 60,
        "low": 30
    }

    score = mapping.get(severity, 0)

    return {
        "severity": severity.title(),
        "risk_score": score
    }


# ---------------------------------------------------
# Executive Summary
# ---------------------------------------------------

@mcp.tool()
def generate_summary(threat: str) -> str:
    """
    Generates a short executive summary.
    """

    return (
        f"The investigation identified a potential {threat}. "
        "Immediate review and remediation are recommended."
    )


# ---------------------------------------------------
# Recommendations
# ---------------------------------------------------

@mcp.tool()
def generate_recommendations(threat: str) -> list:
    """
    Returns security recommendations.
    """

    recommendations = [
        "Review affected systems.",
        "Reset compromised credentials.",
        "Investigate related logs.",
        "Apply latest security patches.",
        "Monitor for additional suspicious activity."
    ]

    return recommendations


# ---------------------------------------------------
# Start Server
# ---------------------------------------------------

if __name__ == "__main__":
    mcp.run()