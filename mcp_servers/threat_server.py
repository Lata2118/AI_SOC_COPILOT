"""
Threat Intelligence MCP Server

Provides cybersecurity threat intelligence tools
for IP addresses, domains and file hashes.

Used by:
- Threat Detection Agent
- Coordinator Agent
"""

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------
# Create MCP Server
# ---------------------------------------------------

mcp = FastMCP("Threat Intelligence MCP Server")


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@mcp.tool()
def health_check() -> str:
    """
    Checks whether the MCP server is running.
    """
    return "Threat Intelligence MCP Server is running successfully."


# ---------------------------------------------------
# IP Reputation Lookup
# ---------------------------------------------------

@mcp.tool()
def ip_lookup(ip: str) -> dict:
    """
    Performs a mock IP reputation lookup.
    """

    malicious_ips = {
        "192.168.1.100": "High",
        "10.10.10.50": "Medium",
        "8.8.8.8": "Low"
    }

    reputation = malicious_ips.get(ip, "Unknown")

    return {
        "ip": ip,
        "reputation": reputation
    }


# ---------------------------------------------------
# Domain Reputation Lookup
# ---------------------------------------------------

@mcp.tool()
def domain_lookup(domain: str) -> dict:
    """
    Performs a mock domain reputation lookup.
    """

    malicious_domains = {
        "malicious.com": "Malicious",
        "phishing-site.com": "Phishing",
        "example.com": "Safe"
    }

    status = malicious_domains.get(domain, "Unknown")

    return {
        "domain": domain,
        "status": status
    }


# ---------------------------------------------------
# File Hash Lookup
# ---------------------------------------------------

@mcp.tool()
def hash_lookup(file_hash: str) -> dict:
    """
    Performs a mock malware hash lookup.
    """

    malicious_hashes = {
        "abcd1234": "Trojan",
        "xyz789": "Ransomware",
        "123456": "Worm"
    }

    detection = malicious_hashes.get(file_hash, "Not Found")

    return {
        "hash": file_hash,
        "detection": detection
    }


# ---------------------------------------------------
# Start Server
# ---------------------------------------------------

if __name__ == "__main__":
    mcp.run()