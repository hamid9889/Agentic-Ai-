import sys
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()


def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-20b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions=[
            "You are a helpful travel research agent.",
            "When searching the web, use concise search queries rather than long phrases.",
            "Provide clean, structured responses with clear markdown formatting.",
        ],
        tool_call_limit=3,
        add_datetime_to_context=True,
    )


if __name__ == "__main__":
    agent = build_agent()
    agent.print_response("Is it safe to travel to UAE today?")