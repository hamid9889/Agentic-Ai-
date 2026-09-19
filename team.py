import sys
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()


def build_team():
    eng_agent = Agent(name="English Agent", role="You answer questions in English")
    chi_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
    hindi_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")

    return Team(
        name="Answer & Translation Team",
        members=[eng_agent, chi_agent, hindi_agent],
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        show_members_responses=True,
        instructions="""All member agents must respond to answer the query in their specific language.
Do not route to just one agent.
Output the response of all agents.""",
    )


if __name__ == "__main__":
    team = build_team()
    team.print_response("What is the capital of India?")


