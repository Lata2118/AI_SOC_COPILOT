from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME
from models.threat_models import ThreatAnalysis
from models.mitre_models import MitreMapping
from models.risk_models import RiskAssessment

client = genai.Client(api_key=GEMINI_API_KEY)

def assess_risk(threat, mitre):

    prompt = f"""
You are a Cyber Risk Analyst.

Threat:
{threat.threat_name}

Severity:
{threat.severity}

Confidence:
{threat.confidence}

MITRE Technique:
{mitre.technique_id} - {mitre.technique_name}

Calculate:

- Risk Score (0-100)
- Severity (Low, Medium, High, Critical)
- Justification

Return only structured data.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=RiskAssessment,
        ),
    )

    return response.parsed