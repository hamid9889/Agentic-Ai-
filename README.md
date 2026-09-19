# ⚡ Enng Agentic Hub (Groq + Gemini)
*Built by Hamid Ansari*

A high-performance multi-agent framework built with **Agno**, powered by **Groq** for lightning-fast inference and **Google Gemini** for multimodal YouTube video intelligence.

---

## 🤖 Agents Architecture

1. **🌐 General Travel & Web Agent (`agent.py`)**
   - **Model:** Groq `openai/gpt-oss-20b`
   - **Tools:** DuckDuckGo Search
   - **Capabilities:** Autonomous real-time travel research, safety advisories, and destination synthesis with loop-engineered query handling.

2. **💰 Financial Research Agent (`finance.py`)**
   - **Model:** Groq `openai/gpt-oss-120b`
   - **Tools:** Native YFinance (Real-time stock pricing, analyst consensus ratings, company profiles, fundamentals) + DuckDuckGo
   - **Capabilities:** Instant financial ratios and analyst recommendations formatted in markdown tables without redundant search loops.

3. **🧠 Stateful Memory Agent (`memory.py`)**
   - **Model:** Groq `openai/gpt-oss-120b`
   - **Storage:** SQLite (`agno.db`) with `enable_agentic_memory=True`
   - **Capabilities:** Autonomous memory extraction, persistence, and profile recollection across user sessions.

4. **👥 Multilingual Team Agent (`team.py`)**
   - **Model:** Groq `openai/gpt-oss-120b`
   - **Team Members:** English Agent 🇬🇧, Chinese Agent 🇨🇳, Hindi Agent 🇮🇳
   - **Capabilities:** Coordinated multi-agent delegation, synthesis, and tri-lingual translation.

5. **🎥 YouTube Video Analyzer (`youtube_analyzer.py`)**
   - **Model:** Google Gemini (`gemini-flash-lite-latest`)
   - **Tools:** YouTubeTools (with multi-language `en` + `en-US` transcript extraction)
   - **Capabilities:** Automated video metadata extraction, timestamp segmentation, topic hierarchy, and key learning points.

---

## 🚀 Setup & Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables (`.env`)

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
```

```env
GOOGLE_API_KEY="your_gemini_api_key"
GROQ_API_KEY="your_groq_api_key"
```

---

## 💻 Running the Agents

### Run Individual CLI Agents

```bash
python agent.py
python finance.py
python memory.py
python team.py
python youtube_analyzer.py
```

### Run the Interactive Web Dashboard

```bash
streamlit run ui.py
```

The web dashboard provides a glassmorphism UI with real-time model diagnostics, sample prompt buttons, user memory inspection, embedded video previews, and execution timers.

