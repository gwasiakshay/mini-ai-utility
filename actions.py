import json
from openai_client import client
from schemas import ArticleSummary
from openai_client import summarize_article
from schemas import RewriteResult
from prompts import REWRITE_PROMPT
from schemas import ExtractResult
from prompts import EXTRACT_PROMPT


def summarize_action(text: str) -> ArticleSummary:
    raw_output = summarize_article(text)

    parsed_json = json.loads(raw_output)
    return ArticleSummary(**parsed_json)


def rewrite_action(text: str) -> RewriteResult:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": REWRITE_PROMPT},
            {"role": "user", "content": text},
        ],
    )

    raw_output = response.choices[0].message.content
    parsed = json.loads(raw_output)

    return RewriteResult(**parsed)


def extract_action(text: str) -> ExtractResult:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": EXTRACT_PROMPT},
            {"role": "user", "content": text},
        ],
    )

    raw_output = response.choices[0].message.content
    parsed = json.loads(raw_output)

    return ExtractResult(**parsed)
