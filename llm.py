import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def ask_llm(prompt, temperature=0.3, max_tokens=600):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is missing from your .env file."
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful general-purpose AI assistant. "
                    "Answer questions on any topic. Follow the user's "
                    "requested language, format, and programming language."
                )
            },
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens
    )

    return response.choices[0].message.content
