import os


from dotenv import load_dotenv

from google import genai
from google.genai import types


load_dotenv()

private_api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=private_api_key)

MODEL_NAME = "gemini-2.5-flash"

prompt = "prove the pythagorus theorem text by text"

response = client.models.generate_content(  # type: ignore
    model=MODEL_NAME,
    contents=prompt,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=1024,
            include_thoughts=True,
        )
    ),
)


for part in response.candidates[0].content.parts:
    if not part.text:
        continue
    if part.thought:
        print("Thought summary:")
        print(part.text)
        print()
    else:
        print("Answer:")
        print(part.text)
        print()
