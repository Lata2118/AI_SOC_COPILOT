from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME

from models.log_models import LogAnalysis
from models.threat_models import ThreatAnalysis
from models.mitre_models import MitreMapping
from models.risk_models import RiskAssessment
from models.report_models import IncidentReport

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_report(log, threat, mitre, risk):

    prompt = f"""
You are a Senior SOC Incident Responder.

Create a professional incident report.

Log Summary:
{log.summary}

Threat:
{threat.threat_name}

Severity:
{threat.severity}

Recommendation:
{threat.recommendation}

MITRE:
{mitre.technique_id}
{mitre.technique_name}

Risk Score:
{risk.risk_score}

Risk Severity:
{risk.severity}

Return:

- incident_title
- executive_summary
- findings
- mitre_mapping
- risk_assessment
- recommendations
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=IncidentReport,
        ),
    )

    return response.parsed