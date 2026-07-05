\# AI SOC Copilot Architecture



\## Overview



AI SOC Copilot follows a modular multi-agent architecture where specialized AI agents collaborate to investigate cybersecurity incidents.



The application is designed to separate responsibilities into independent agents while allowing a Coordinator Agent to orchestrate the complete investigation workflow.



\---



\## Architecture Components



\### Streamlit Dashboard



The Streamlit dashboard serves as the user interface.



Responsibilities:



\- Upload security log files

\- Display investigation results

\- Visualize risk score

\- Display MITRE ATT\&CK mapping

\- Download incident report



\---



\### Coordinator Agent



The Coordinator Agent orchestrates the entire workflow.



Responsibilities:



\- Receives uploaded logs

\- Invokes each specialized AI agent

\- Aggregates results

\- Returns a complete investigation



\---



\### Specialized AI Agents



\#### Log Analysis Agent



\- Parses uploaded logs

\- Extracts suspicious events

\- Identifies important indicators



\#### Threat Detection Agent



\- Detects attack patterns

\- Identifies possible threats

\- Provides remediation suggestions



\#### MITRE Mapping Agent



\- Maps threats to MITRE ATT\&CK techniques

\- Explains attacker behavior



\#### Risk Assessment Agent



\- Calculates overall risk score

\- Determines severity level



\#### Report Generation Agent



\- Produces executive summary

\- Generates findings

\- Provides recommendations



\---



\## Model Context Protocol (MCP)



The project includes three MCP servers implemented using the official MCP Python SDK.



\### Threat MCP Server



Provides threat intelligence tools including:



\- IP Reputation

\- Domain Reputation

\- Malware Hash Lookup



\### MITRE MCP Server



Provides:



\- MITRE ATT\&CK technique lookup

\- Tactic mapping

\- Technique explanations



\### Report MCP Server



Provides:



\- Risk calculation

\- Executive summary generation

\- Recommendation generation



These servers demonstrate how cybersecurity tools can be exposed using the Model Context Protocol.



\---



\## AI Service



Google Gemini API powers the reasoning capabilities of the agents.



Gemini is responsible for:



\- Threat reasoning

\- MITRE mapping

\- Risk analysis

\- Executive report generation



\---



\## Workflow



1\. User uploads log file.

2\. Coordinator Agent starts investigation.

3\. Log Analysis Agent extracts suspicious activity.

4\. Threat Detection Agent identifies attacks.

5\. MITRE Agent maps ATT\&CK techniques.

6\. Risk Agent calculates severity.

7\. Report Agent generates incident report.

8\. Dashboard displays results.



\---



\## Benefits



\- Modular Architecture

\- Easy to Extend

\- Reusable AI Agents

\- MCP-based Tool Design

\- Clear Separation of Responsibilities

