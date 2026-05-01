import streamlit as st
import random

st.set_page_config(page_title="KronosAI 🚀", page_icon="🧠", layout="wide")

# ─────────────────────────────
# SIDEBAR
# ─────────────────────────────
with st.sidebar:
    st.title("⚡ KronosAI")

    mode = st.radio(
        "Choose Mode",
        [
            "🧠 AI Tutor",
            "💼 Jobs",
            "🎯 Quiz",
        ]
    )

# ─────────────────────────────
# 🧠 FULL AI CURRICULUM ENGINE (YOUR MODULES)
# ─────────────────────────────
AI_SYLLABUS = {
    "python": """
MODULE 1: Python for AI
- Syntax, Variables, Data Types
- Loops & Functions
- File Handling, JSON, APIs
- pip & Virtual Environments
- Jupyter & VS Code
Example: Python is used in ML models like recommendation systems.
""",

    "ai models": """
MODULE 2: AI Foundations
- AI vs ML vs DL vs NLP vs CV
- Transformers overview
- Pretrained vs Fine-tuned models
- Industry use cases (Netflix, Tesla, Google)
""",

    "prompt": """
MODULE 3: Prompt Engineering
- System / User / Assistant roles
- Zero-shot, Few-shot prompting
- Chain-of-Thought
- JSON structured prompts
Example: ChatGPT prompt design
""",

    "llm": """
MODULE 5: Large Language Models
- GPT, Claude, LLaMA, Mistral
- Training vs Inference
- Hallucination & Bias
- Limitations & use cases
""",

    "rag": """
MODULE 9: RAG Systems
- Retrieval Augmented Generation
- Embeddings + Vector DB
- PDF Q&A systems
Example: ChatGPT + your documents
""",

    "langchain": """
MODULE 10: LangChain & Agents
- Chains, Tools, Memory
- Multi-agent systems
- Workflow automation
Example: AI chatbot with tools
""",

    "tools": """
MODULE 11: AI Tools
- ChatGPT, Claude, Gemini
- Cursor, Copilot, Replit AI
- n8n, Zapier, Make.com
- Midjourney, DALL·E, Runway
""",

    "agents": """
MODULE 16: Agentic AI
- AI agents that plan + execute tasks
- Multi-agent systems
- Research automation
Example: AutoGPT style systems
"""
}

# ─────────────────────────────
# 🧠 AI TUTOR (SMART ENGINE)
# ─────────────────────────────
if mode == "🧠 AI Tutor":

    st.title("🧠 KronosAI Tutor (Full AI Syllabus)")

    q = st.text_input("Ask anything (Python / AI / ML / GenAI / Tools)")

    if q:

        found = False

        for k, v in AI_SYLLABUS.items():
            if k in q.lower():
                st.success(v)

                st.info("""
📌 Real Example:
Netflix → ML recommendation system  
ChatGPT → LLM + RAG system  
Tesla → AI + Computer Vision  

📌 Coding Example:
Python + scikit-learn + transformers
""")
                found = True
                break

        if not found:
            st.warning("""
I cover full AI stack:

✔ Python for AI  
✔ Machine Learning  
✔ Deep Learning  
✔ GenAI / LLMs  
✔ Prompt Engineering  
✔ RAG Systems  
✔ LangChain / Agents  
✔ AI Tools (Copilot, ChatGPT, n8n)  

👉 Please ask more specific topic
""")

# ─────────────────────────────
# 💼 JOB ENGINE (ALL COMPANIES + ROLES)
# ─────────────────────────────
elif mode == "💼 Jobs":

    st.title("💼 AI Job Engine")

    role = st.selectbox("Role", [
        "Data Analyst",
        "AI Engineer",
        "ML Engineer",
        "GenAI Engineer",
        "Python Developer",
        "Business Analyst"
    ])

    exp = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])

    JOBS = {
        "Fresher": [
            "TCS - Graduate Trainee",
            "Infosys - Analyst",
            "Wipro - Python Developer",
            "Capgemini - Data Analyst"
        ],
        "1-3 Years": [
            "Accenture - AI Engineer",
            "Amazon - Data Analyst",
            "IBM - ML Engineer",
            "Cognizant - Developer"
        ],
        "3+ Years": [
            "Google - Senior AI Engineer",
            "Microsoft - Data Scientist",
            "Meta - ML Engineer",
            "Startup - GenAI Engineer"
        ]
    }

    st.subheader("🔥 Recommended Jobs")

    for j in JOBS[exp]:
        st.success(j)

    st.info("💡 Apply daily 10–20 jobs + build AI projects + GitHub profile")

# ─────────────────────────────
# 🎯 QUIZ ENGINE (AI LEARNING GAME)
# ─────────────────────────────
elif mode == "🎯 Quiz":

    st.title("🎯 KronosAI Learning Game")

    quizzes = [
        ("What is AI?", "Machines simulating human intelligence"),
        ("What is ML?", "Learning from data"),
        ("What is DL?", "Neural networks with layers"),
        ("What is GenAI?", "Creates text/images/code"),
        ("What is RAG?", "LLM + retrieval system"),
        ("What is LLM?", "Large language model like GPT"),
        ("What is Python used for AI?", "Building ML models"),
        ("What is overfitting?", "Model memorizes training data")
    ]

    q, ans = random.choice(quizzes)

    st.subheader(q)

    user = st.text_input("Your Answer")

    if st.button("Check"):

        if ans.lower() in user.lower():
            st.success("Correct 🎉")
        else:
            st.error(f"Wrong ❌ Answer: {ans}")

        st.info("💡 Keep learning modules daily to master AI")
