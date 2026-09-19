import sys
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()


def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[
            YFinanceTools(
                enable_stock_price=True,
                enable_analyst_recommendations=True,
                enable_company_info=True,
                enable_stock_fundamentals=True,
            ),
            DuckDuckGoTools(),
        ],
        markdown=True,
        add_datetime_to_context=True,
        description="Financial analyst specializing in equities, analyst recommendations, and market data.",
        instructions=[
            "Use YFinance tools for stock prices, analyst consensus, and company metrics.",
            "Use web search only when recent news or contextual market commentary is requested.",
            "Present financial data in clean markdown tables where applicable.",
        ],
        tool_call_limit=5,
    )


if __name__ == "__main__":
    agent = build_agent()
    agent.print_response("Share the MSFT stock price and analyst recommendations")


