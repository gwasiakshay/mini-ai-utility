# Mini AI Utility — Agent-Based Text Processor

A local Python AI utility that processes text using Large Language Models.
The project was built incrementally to explore **manual agent design** and
**framework-based agent abstractions**.

The utility can:
- summarize text
- rewrite text
- extract structured information

---

## Features

- Reads input from file or CLI
- Uses LLMs via OpenAI-compatible APIs (OpenRouter supported)
- Returns structured JSON outputs
- Validates responses using Pydantic
- Clean, modular project structure
- Multiple agent implementations for comparison

---

## Project Structure

mini-ai-utility/
├── main.py # Manual agent entry point
├── agent.py # Manual agent logic (intent + routing)
├── actions.py # LLM-backed actions
├── prompts.py # Prompts for manual agent
├── schemas.py # Pydantic schemas
├── agent_pydanticai.py # PydanticAI agent implementation
├── agent_langchain.py # LangChain router-style implementation
├── input.txt # Sample input
├── requirements.txt
├── .env # API keys (not committed)


---

## Agent Implementations

This project implements the same agent behavior in three different ways to
understand system design trade-offs.

### Manual Agent (Pure Python)

- Explicit intent classification and routing
- Full control over prompts and execution flow
- Structured output validation using Pydantic
- Most transparent and debuggable
- More boilerplate code

### PydanticAI Agent

- Declarative tool definitions
- Automatic prompt generation and schema enforcement
- Async-first execution model
- Less explicit routing logic
- Best suited for production safety and correctness

### LangChain Agent

- Explicit routing using chains
- Flexible composition of multi-step workflows
- Minimal built-in validation unless added manually
- Useful for complex orchestration scenarios

---

## Agent Design Comparison

| Aspect        | Manual Agent | PydanticAI Agent | LangChain Agent |
|--------------|-------------|------------------|-----------------|
| Routing      | Explicit     | Abstracted       | Explicit        |
| Execution    | Synchronous  | Asynchronous     | Synchronous     |
| Validation   | Manual       | Automatic        | Optional        |
| Error Model  | Logical      | Framework-level  | Type-flow based |
| Best For     | Learning & Control | Production Safety | Complex Workflows |

---

## Design Philosophy

The project was intentionally built **without frameworks first** to understand
the fundamentals of AI agent design:
- when to use LLMs
- when to rely on deterministic logic
- how to structure and validate outputs

Frameworks were introduced only after the manual implementation to clearly
understand what they abstract and why they exist.

---

## How to Run

### Manual Agent
```bash
python main.py input.txt
