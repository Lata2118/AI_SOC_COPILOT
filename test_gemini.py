from google import genai
from config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="Introduce yourself in one sentence."
)

print(response.text)