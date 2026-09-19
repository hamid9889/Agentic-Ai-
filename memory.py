import sys
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()

db = SqliteDb(db_file="agno.db")


def build_agent():
    return Agent(
        db=db,
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        add_history_to_context=True,
        enable_agentic_memory=True,
    )


if __name__ == "__main__":
    db.clear_memories()
    agent = build_agent()

    user_id = "Hamid@gmail.com"
    agent.print_response("I am Hamid & I am an AI / ML engineer.", user_id=user_id)
    agent.print_response("who am I?", user_id=user_id)

    memories = agent.get_user_memories(user_id=user_id)
    print("\nMEMORIES:")
    pprint(memories)


