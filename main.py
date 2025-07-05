import os
import requests
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(usr_input: str):
    """
    Function to generate a post for X (formerly Twitter) based on user input,
    using an AI /LLM (Large Language Model) to create engaging content.
    """
    payload = {
        "model": "gpt-4o",
        "input": "..."
    }
    response = requests.post("https://api.openai.com/v1/responses", 
        json=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {OPENAI_API_KEY}"
            }
        )
    return response.text
            

def main():
    # user input => AI (LLM) to generate X post => output post

    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print(f"Generated X post: {x_post}")


if __name__ == "__main__":
    main()
