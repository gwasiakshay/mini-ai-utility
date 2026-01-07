import os
from dotenv import load_dotenv
from typing import List

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

summarize_prompt = PromptTemplate.from_template(
    "Summarize the text and list key points:\n{text}"
)

rewrite_prompt = PromptTemplate.from_template(
    "Rewrite the text to be clearer and more professional:\n{text}"
)

extract_prompt = PromptTemplate.from_template(
    "Extract key requirements or important items as bullet points:\n{text}"
)


summarize_chain = summarize_prompt | llm
rewrite_chain = rewrite_prompt | llm
extract_chain = extract_prompt | llm


def route(text: str):
    lower = text.lower()

    if "requirements" in lower:
        return extract_chain

    if len(lower.split()) > 60:
        return summarize_chain

    return rewrite_chain


# router = RunnableLambda(route)


def run_langchain_agent(text: str):
    chain = route(text)
    result = chain.invoke({"text": text})  # returns a chain
    return result.content


if __name__ == "__main__":
    test_input = """
    Job Requirements:
    - Strong Python skills
    - Experience with APIs
    - Familiarity with SQL
    """

    output = run_langchain_agent(test_input)
    print("\n=== LANGCHAIN OUTPUT ===\n")
    print(output)
