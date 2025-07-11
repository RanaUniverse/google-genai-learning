from dotenv import load_dotenv
import os

load_dotenv()

# When you need the value
value = os.environ.get("GEMINI_API_KEY")


def main():
    print("Hello from google-genai-learning!")
    print("I will use google genai api key now.")
    print("The Private Value is,")
    print(value)


if __name__ == "__main__":
    main()
