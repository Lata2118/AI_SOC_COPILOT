from google import genai
from google.genai import types

from config import GEMINI_API_KEY, MODEL_NAME
from models.log_models import LogAnalysis

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_logs(log_text):

    prompt = f"""
You are an expert SOC Analyst.

Analyze these logs.

Logs:
{log_text}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=LogAnalysis,
        ),
    )

    return response.parsed