from pydantic import BaseModel
from typing import List
from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
import asyncio

# from openai import OpenAI
import os


# Load your OpenRouter key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


agent = Agent(
    model="openai:gpt-4o-mini",
    system_prompt=(
        "You are an AI agent that decides whether to summarize, rewrite, "
        "or extract information from the input. "
        "Use the appropriate tool and return structured output only."
    ),
)


class SummaryOutput(BaseModel):
    summary: str
    key_points: List[str]


class RewriteOutput(BaseModel):
    rewritten_text: str


class ExtractOutput(BaseModel):
    items: List[str]


@agent.tool
def summarize(ctx: RunContext, text: str) -> SummaryOutput:
    """
    Summarize the given text and extract key points.
    """
    return SummaryOutput(summary="...", key_points=[])


@agent.tool
def rewrite(ctx: RunContext, text: str) -> RewriteOutput:
    """
    Rewrite the text to be clearer and more professional.
    """
    return RewriteOutput(rewritten_text="...")


@agent.tool
def extract(ctx: RunContext, text: str) -> ExtractOutput:
    """
    Extract key requirements or important items from the text.
    """
    return ExtractOutput(items=[])


async def run_agent_framework(user_input: str):
    result = await agent.run(user_input)
    return result.output


if __name__ == "__main__":
    test_input = """
    Job Requirements:
    - Strong Python skills
    - Experience with APIs
    - Familiarity with SQL
    - Ability to work independently
    """

    output = asyncio.run(run_agent_framework(test_input))
    print("\n=== PYDANTICAI OUTPUT ===\n")
    print(output)
