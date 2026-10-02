from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(message):

    response = client.responses.create(
        model="openrouter/free",
        input=message
    )

    return response.output_text

def understand_command(message):

    response = client.responses.create(
        model="openrouter/free",
        input=f"""
You are BEASTAG, a PC assistant.

Read the user's request and decide if they want one of these actions:

- open chrome
- open notepad
- open calculator
- open spotify

If they want one of these actions, reply with ONLY the exact command.
If they are not asking for a PC action, reply with ONLY: none

User request: {message}
"""
    )

    return response.output_text.strip().lower()

print(understand_command("open chrome"))