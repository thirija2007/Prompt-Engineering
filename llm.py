import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct"


def ask_llm(prompt, temperature=0.3, max_tokens=600):

    token = os.getenv("HF_TOKEN")

    if not token:
        raise RuntimeError("HF_TOKEN is not being loaded from .env")

    client = InferenceClient(
        api_key=token
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful React programming assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content