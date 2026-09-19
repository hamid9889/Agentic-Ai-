import sys
import streamlit as st
from dotenv import load_dotenv

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()

st.set_page_config(
    page_title="Enng Agentic Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Classy & Modern SaaS Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    h1, h2, h3, h4 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600;
        letter-spacing: -0.02em;
    }

    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 2.5rem;
        max-width: 1120px;
    }

    /* Classy Header */
    .page-header {
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        position: relative;
    }

    .page-title {
        font-size: 1.95rem;
        font-weight: 700;
        letter-spacing: -0.025em;
        background: linear-gradient(90deg, #ffffff 0%, #e2e8f0 60%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
    }

    .page-subtitle {
        color: #94a3b8;
        font-size: 0.96rem;
        font-weight: 400;
        margin: 0;
    }

    .quick-label {
        font-size: 0.83rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: #64748b;
        margin-bottom: 8px;
    }

    /* Brand Header Box */
    .brand-container {
        padding: 10px 14px 16px 14px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.6) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.35);
        margin-bottom: 18px;
    }

    .brand-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .brand-author {
        font-size: 0.78rem;
        font-weight: 500;
        color: #38bdf8;
        letter-spacing: 0.02em;
        margin-top: 2px;
        display: flex;
        align-items: center;
        gap: 4px;
    }

    /* Memory items */
    .memory-item {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 10px;
        padding: 12px 16px;
        margin-bottom: 10px;
        color: #e2e8f0;
        font-size: 0.92rem;
        transition: border-color 0.2s ease;
    }

    .memory-item:hover {
        border-color: rgba(59, 130, 246, 0.4);
    }

    /* Interactive Buttons */
    div.stButton > button:first-child {
        border-radius: 9px;
        font-weight: 500;
        padding: 0.48rem 1.25rem;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    div.stButton > button:first-child:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
    }

    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #4338ca 100%);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }

    /* Footer tag */
    .sidebar-footer {
        margin-top: 30px;
        padding-top: 14px;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        text-align: center;
        color: #64748b;
        font-size: 0.76rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource(show_spinner=False)
def get_general_agent():
    from agent import build_agent
    return build_agent()


@st.cache_resource(show_spinner=False)
def get_finance_agent():
    from finance import build_agent
    return build_agent()


@st.cache_resource(show_spinner=False)
def get_memory_agent():
    from memory import build_agent
    return build_agent()


@st.cache_resource(show_spinner=False)
def get_team_agent():
    from team import build_team
    return build_team()


@st.cache_resource(show_spinner=False)
def get_youtube_agent():
    from youtube_analyzer import build_youtube_agent
    return build_youtube_agent()


# ==============================
# SIDEBAR NAVIGATION
# ==============================
with st.sidebar:
    st.markdown(
        """
        <div class="brand-container">
            <div class="brand-title">
                <span>⚡</span> Enng Agentic Hub
            </div>
            <div class="brand-author">
                <span>✦</span> Built by Hamid Ansari
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("Select an agent:")

    selected_agent = st.radio(
        "Navigation",
        [
            "General",
            "Finance",
            "Memory",
            "Team",
            "YouTube Analyzer",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")

    with st.expander("System Status", expanded=False):
        import os
        has_groq = bool(os.getenv("GROQ_API_KEY"))
        has_google = bool(os.getenv("GOOGLE_API_KEY"))

        st.write("• Groq Service:", "Connected" if has_groq else "Key Missing")
        st.write("• Gemini Service:", "Connected" if has_google else "Key Missing")
        st.write("• Memory Database:", "Active")

        if st.button("Reset Session Cache", use_container_width=True):
            st.cache_resource.clear()
            st.rerun()

    st.markdown(
        """
        <div class="sidebar-footer">
            Enng Agentic Hub<br>
            <span style="color: #94a3b8; font-weight: 500;">Built by Hamid Ansari</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==============================
# 1. GENERAL AGENT
# ==============================
if selected_agent == "General":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-title">General Assistant</div>
            <p class="page-subtitle">Search the web and research travel, destinations, and general inquiries.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "gen_query" not in st.session_state:
        st.session_state.gen_query = ""

    st.markdown('<p class="quick-label">Try a prompt:</p>', unsafe_allow_html=True)
    q_col1, q_col2, q_col3 = st.columns(3)
    if q_col1.button("Is it safe to travel to UAE?", use_container_width=True):
        st.session_state.gen_query = "Is it safe to travel to UAE today?"
        st.rerun()
    if q_col2.button("Top Autumn Spots in Japan", use_container_width=True):
        st.session_state.gen_query = "What are the top 3 spots to see autumn foliage in Japan?"
        st.rerun()
    if q_col3.button("Switzerland Travel Tips", use_container_width=True):
        st.session_state.gen_query = "Best budget travel tips for visiting Switzerland"
        st.rerun()

    query = st.text_input(
        "Ask a question:",
        value=st.session_state.gen_query,
        placeholder="Ask about a destination, advisory, or general topic...",
        label_visibility="collapsed",
        key="input_general_query",
    )

    if st.button("Search", type="primary") and query.strip():
        with st.spinner("Researching..."):
            try:
                agent = get_general_agent()
                response = agent.run(query)
                st.markdown("---")
                st.markdown(response.content)
            except Exception as e:
                st.error("Unable to complete request.")
                st.caption(str(e))


# ==============================
# 2. FINANCE AGENT
# ==============================
elif selected_agent == "Finance":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-title">Financial Research</div>
            <p class="page-subtitle">Real-time stock quotes, fundamental metrics, and analyst consensus data.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "fin_query" not in st.session_state:
        st.session_state.fin_query = ""

    st.markdown('<p class="quick-label">Quick tickers:</p>', unsafe_allow_html=True)
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    if f_col1.button("Microsoft (MSFT)", use_container_width=True):
        st.session_state.fin_query = "Share the MSFT stock price and analyst recommendations"
        st.rerun()
    if f_col2.button("NVIDIA (NVDA)", use_container_width=True):
        st.session_state.fin_query = "Share the NVDA stock price and key financial ratios"
        st.rerun()
    if f_col3.button("Apple (AAPL)", use_container_width=True):
        st.session_state.fin_query = "Share the AAPL stock price and analyst recommendations"
        st.rerun()
    if f_col4.button("Tesla (TSLA)", use_container_width=True):
        st.session_state.fin_query = "Share the TSLA stock price and fundamentals"
        st.rerun()

    fin_input = st.text_input(
        "Stock inquiry:",
        value=st.session_state.fin_query,
        placeholder="Search a company or ask a market question...",
        label_visibility="collapsed",
        key="input_fin_query",
    )

    if st.button("Analyze Stock", type="primary") and fin_input.strip():
        with st.spinner("Fetching market data..."):
            try:
                agent = get_finance_agent()
                response = agent.run(fin_input)
                st.markdown("---")
                st.markdown(response.content)
            except Exception as e:
                st.error("Unable to complete financial research.")
                st.caption(str(e))


# ==============================
# 3. MEMORY AGENT
# ==============================
elif selected_agent == "Memory":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-title">Memory Assistant</div>
            <p class="page-subtitle">An agent that remembers facts about you across conversations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    from agno.db.sqlite import SqliteDb
    db = SqliteDb(db_file="agno.db")

    prof_col1, prof_col2 = st.columns([3, 1])
    with prof_col1:
        user_id = st.text_input("Profile ID:", value="Hamid@gmail.com", help="Identifies your session memory.")
    with prof_col2:
        st.write("")
        st.write("")
        if st.button("Clear Memories", use_container_width=True):
            try:
                existing = db.get_user_memories(user_id=user_id)
                if existing:
                    ids = [m.memory_id for m in existing if hasattr(m, "memory_id")]
                    db.delete_user_memories(memory_ids=ids, user_id=user_id)
                    st.success("Memories cleared.")
                else:
                    st.info("No memories found to clear.")
            except Exception as e:
                st.error(f"Error clearing memories: {e}")

    if "mem_query" not in st.session_state:
        st.session_state.mem_query = ""

    st.markdown('<p class="quick-label">Suggested messages:</p>', unsafe_allow_html=True)
    m_col1, m_col2, m_col3 = st.columns(3)
    if m_col1.button("Tell: I am Hamid, AI Engineer", use_container_width=True):
        st.session_state.mem_query = "I am Hamid & I am an AI / ML engineer."
        st.rerun()
    if m_col2.button("Ask: Who am I?", use_container_width=True):
        st.session_state.mem_query = "Who am I?"
        st.rerun()
    if m_col3.button("Tell: I build AI applications", use_container_width=True):
        st.session_state.mem_query = "I love building multi-agent AI applications."
        st.rerun()

    user_msg = st.text_input(
        "Chat with Memory Agent:",
        value=st.session_state.mem_query,
        placeholder="Tell the agent something about yourself or ask what it remembers...",
        label_visibility="collapsed",
        key="input_mem_query",
    )

    if st.button("Send Message", type="primary") and user_msg.strip():
        with st.spinner("Processing..."):
            try:
                agent = get_memory_agent()
                response = agent.run(user_msg, user_id=user_id)
                st.markdown("---")
                st.markdown(response.content)
            except Exception as e:
                st.error("Unable to process message.")
                st.caption(str(e))

    st.markdown("---")
    st.markdown("##### Your Saved Memories")
    try:
        agent = get_memory_agent()
        memories = agent.get_user_memories(user_id=user_id)
        if memories:
            for m in memories:
                st.markdown(f'<div class="memory-item">• {m.memory}</div>', unsafe_allow_html=True)
        else:
            st.caption("No memories saved yet for this profile.")
    except Exception:
        st.caption("No memories found.")


# ==============================
# 4. TEAM AGENT
# ==============================
elif selected_agent == "Team":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-title">Multilingual Team</div>
            <p class="page-subtitle">Collaborative responses synthesized across English, Chinese, and Hindi agents.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "team_query" not in st.session_state:
        st.session_state.team_query = ""

    st.markdown('<p class="quick-label">Sample topics:</p>', unsafe_allow_html=True)
    t_col1, t_col2, t_col3 = st.columns(3)
    if t_col1.button("Capital of India", use_container_width=True):
        st.session_state.team_query = "What is the capital of India?"
        st.rerun()
    if t_col2.button("What is an AI Agent?", use_container_width=True):
        st.session_state.team_query = "What is an AI agent and how does it work?"
        st.rerun()
    if t_col3.button("Why is the sky blue?", use_container_width=True):
        st.session_state.team_query = "Why is the sky blue during the day?"
        st.rerun()

    team_msg = st.text_input(
        "Question for the team:",
        value=st.session_state.team_query,
        placeholder="Ask a question for the team...",
        label_visibility="collapsed",
        key="input_team_query",
    )

    if st.button("Ask Team", type="primary") and team_msg.strip():
        with st.spinner("Coordinating team members..."):
            try:
                team = get_team_agent()
                response = team.run(team_msg)
                st.markdown("---")
                st.markdown(response.content)
            except Exception as e:
                st.error("Team coordination encountered an error.")
                st.caption(str(e))


# ==============================
# 5. YOUTUBE ANALYZER
# ==============================
elif selected_agent == "YouTube Analyzer":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-title">YouTube Video Analyzer</div>
            <p class="page-subtitle">Extract video overviews, topics, and timestamps directly from video content.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "yt_url" not in st.session_state:
        st.session_state.yt_url = "https://www.youtube.com/watch?v=JkaxUblCGz0"

    st.markdown('<p class="quick-label">Sample video:</p>', unsafe_allow_html=True)
    y_col1, _ = st.columns([1, 2])
    with y_col1:
        if st.button("Netflix: Our Planet | Forests", use_container_width=True):
            st.session_state.yt_url = "https://www.youtube.com/watch?v=JkaxUblCGz0"
            st.rerun()

    video_url = st.text_input(
        "YouTube Video URL:",
        value=st.session_state.yt_url,
        placeholder="Paste YouTube URL here...",
        label_visibility="collapsed",
        key="input_yt_url",
    )

    if video_url:
        with st.expander("Video Preview", expanded=False):
            try:
                st.video(video_url)
            except Exception:
                st.caption("Preview unavailable for this URL.")

    if st.button("Analyze Video", type="primary") and video_url.strip():
        with st.spinner("Analyzing video content and generating timestamps..."):
            try:
                agent = get_youtube_agent()
                response = agent.run(f"Analyze this video: {video_url}")
                st.markdown("---")
                st.markdown(response.content)
            except Exception as e:
                st.error("Unable to analyze video.")
                st.caption(str(e))