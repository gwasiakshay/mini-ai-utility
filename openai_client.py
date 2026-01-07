import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create an OpenAI client BUT pointed to OpenRouter
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",  # optional but recommended by OpenRouter
        "X-Title": "local-testing",
    },
)


def summarize_article(article_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that summarizes articles. "
                    "Return ONLY valid JSON. "
                    "Do not include explanations, markdown, or extra text. "
                    "The JSON must exactly match this schema:\n"
                    "{ summary: string, key_points: string[] }"
                ),
            },
            {
                "role": "user",
                "content": article_text,
            },
        ],
    )
    return response.choices[0].message.content
