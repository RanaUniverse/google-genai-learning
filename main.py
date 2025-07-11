import os


from dotenv import load_dotenv

from google import genai


load_dotenv()

private_api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=private_api_key)

MODEL_NAME = "gemini-2.5-flash"

prompt = "How old the our univers is? say with appropriate emoji."

response = client.models.generate_content(  # type: ignore
    model=MODEL_NAME,
    contents=prompt,
)
print(response.text)
