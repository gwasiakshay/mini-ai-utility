from agent import run_agent
import sys


def read_input():
    path = "input.txt"

    if len(sys.argv) > 1:
        candidate = sys.argv[1]
        if not candidate.startswith("--"):
            path = candidate

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    user_input = read_input()
    result = run_agent(user_input)

    print("\n=== AGENT OUTPUT ===\n")
    print(result)
