import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from sys import argv

def main():
    user_prompt = argv[1] if len(argv) > 1 else None
    if not user_prompt:
        print("No prompt provided")
        os._exit(1)

    verbose = len(argv) > 2 and argv[2] == "--verbose"

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(response.text)

    if verbose:
        print("\n")
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()