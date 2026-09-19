import sys
from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()


def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Gemini(id="gemini-flash-lite-latest"),
        tools=[YouTubeTools(languages=["en", "en-US"])],
        instructions=dedent("""\
            You are a detailed YouTube video content analyst.
            When analyzing a video, provide:
            1. Overview: Title, channel, and high-level premise.
            2. Key Topics & Timestamps: Important transitions, key moments, and formatted time markers.
            3. Takeaways: Core insights and practical takeaways from the content.
            Use concise, well-structured markdown.
        """),
        tool_call_limit=3,
        add_datetime_to_context=True,
        markdown=True,
    )


if __name__ == "__main__":
    youtube_agent = build_youtube_agent()
    youtube_agent.print_response(
        "Analyze this video: https://www.youtube.com/watch?v=JkaxUblCGz0"
    )


