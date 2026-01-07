from actions import summarize_action, rewrite_action, extract_action
from enum import Enum


class Intent(str, Enum):
    SUMMARIZE = "summarize"
    EXTRACT = "extract"
    REWRITE = "rewrite"


def analyze_intent(user_input: str) -> Intent:
    text = user_input.lower()
    word_count = len(text.split())

    if any(word in text for word in ["requirements", "responsibilities", "skills"]):
        return Intent.EXTRACT

    if word_count > 60:
        return Intent.SUMMARIZE

    return Intent.REWRITE


def run_agent(user_input: str):
    intent = analyze_intent(user_input)

    if intent == Intent.SUMMARIZE:
        result = summarize_action(user_input)
        return result.model_dump_json(indent=2)

    if intent == Intent.EXTRACT:
        result = extract_action(user_input)
        return result.model_dump_json(indent=2)

    if intent == Intent.REWRITE:
        result = rewrite_action(user_input)
        return result.model_dump_json(indent=2)

    raise ValueError(f"Unhandled intent: {intent}")
