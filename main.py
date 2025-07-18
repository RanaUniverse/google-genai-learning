import os

from dotenv import load_dotenv

from google import genai

load_dotenv()

private_api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=private_api_key)
MODEL_NAME = "gemini-2.5-flash"


# prompt = "state pythogorus themorem in math in 15 word"
# response = client.models.generate_content(  # type: ignore
#     model=MODEL_NAME,
#     contents=prompt,
# )
# print(response.text)


def answer_question_from_ai(question: str) -> str | None:
    """
    I will call this function in need time
    which will allow a output a which i will use later
    """

    response = client.models.generate_content(  # type: ignore
        model=MODEL_NAME,
        contents=question,
    )

    if not response.text:
        return None

    answer = f"{response.text}" f"\n\n\n" f"-RanaUniverse"

    return answer


if __name__ == "__main__":
    
    question = "What is ai say in 10 word?"

    ai_response = answer_question_from_ai(question)
    print(ai_response)
    print("Thanks")
