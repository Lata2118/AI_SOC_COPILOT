from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME
from models.log_models import LogAnalysis
from models.threat_models import ThreatAnalysis

client = genai.Client(api_key=GEMINI_API_KEY)

def detect_threat(log_analysis: LogAnalysis):

    prompt = f"""
You are an experienced SOC Threat Analyst.

Based on the following analysis:

Attack Type: {log_analysis.attack_type}

Failed Login Count: {log_analysis.failed_login_count}

Suspicious IPs:
{log_analysis.suspicious_ips}

Summary:
{log_analysis.summary}

Return ONLY:

- Threat Name
- Severity (Low, Medium, High, Critical)
- Confidence (0-100)
- Recommendation
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ThreatAnalysis,
        ),
    )

    return response.parsed