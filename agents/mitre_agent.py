from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME
from models.threat_models import ThreatAnalysis
from models.mitre_models import MitreMapping

client = genai.Client(api_key=GEMINI_API_KEY)

def map_mitre(threat: ThreatAnalysis):

    prompt = f"""
You are a cybersecurity expert specializing in the MITRE ATT&CK framework.

Threat Name:
{threat.threat_name}

Severity:
{threat.severity}

Recommendation:
{threat.recommendation}

Map this threat to the most appropriate MITRE ATT&CK technique.

Return:

- tactic
- technique_id
- technique_name
- explanation
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=MitreMapping,
        ),
    )

    return response.parsed