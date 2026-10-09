import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load API key from the project folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

def ask_llm(prompt, temperature=0.3, max_tokens=600):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Groq API key missing. Check the .env file."
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful general-purpose AI assistant. "
                    "Answer the user's actual question on any topic. "
                    "Use clear language and provide code when requested."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens
    )

    return response.choices[0].message.content
