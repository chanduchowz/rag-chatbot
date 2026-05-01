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
            "📄 Resume Builder",
            "🌐 Portfolio Builder"
        ]
    )

# ─────────────────────────────
# FULL AI SYLLABUS ENGINE
# ─────────────────────────────
AI_SYLLABUS = {
    "python": """
MODULE 1: Python for AI
- Syntax, Variables, Data Types
- Loops, Functions
- File Handling, JSON, APIs
- Virtual Environments, pip
- Jupyter, VS Code
Example: Python powers ML models like recommendation systems
""",

    "ai": """
MODULE 2: AI Foundations
- AI vs ML vs DL vs NLP vs CV
- Real-world AI (Netflix, Tesla, Google)
- Pretrained vs Fine-tuned models
""",

    "prompt": """
MODULE 3: Prompt Engineering
- System/User/Assistant roles
- Zero-shot, Few-shot
- Chain-of-Thought prompting
- JSON structured prompts
""",

    "llm": """
MODULE 5: Large Language Models
- GPT, Claude, LLaMA, Mistral
- Training vs Inference
- Hallucinations & bias
""",

    "rag": """
MODULE 9: RAG Systems
- Retrieval Augmented Generation
- Embeddings + Vector DB
- Chat with PDFs
""",

    "langchain": """
MODULE 10: LangChain & Agents
- Chains, Tools, Memory
- Agent workflows
- Multi-step AI systems
""",

    "tools": """
MODULE 11: AI Tools Ecosystem
- ChatGPT, Claude, Gemini
- Copilot, Cursor, Replit AI
- n8n, Zapier, Make.com
- Midjourney, DALL·E
""",

    "agents": """
MODULE 16: Agentic AI Systems
- AI agents that plan & execute tasks
- Multi-agent collaboration
- Autonomous workflows
"""
}

# ─────────────────────────────
# 🧠 AI TUTOR
# ─────────────────────────────
if mode == "🧠 AI Tutor":

    st.title("🧠 KronosAI Tutor")

    q = st.text_input("Ask anything (Python / AI / ML / GenAI / Tools)")

    if q:

        found = False

        for k, v in AI_SYLLABUS.items():
            if k in q.lower():
                st.success(v)

                st.info("""
📌 Real Examples:
- Netflix → Recommendation system (ML)
- ChatGPT → LLM + RAG system
- Tesla → Computer Vision AI

📌 Tools:
Python, scikit-learn, TensorFlow, LangChain
""")
                found = True
                break

        if not found:
            st.warning("""
Covered Topics:
✔ Python for AI  
✔ Machine Learning  
✔ Deep Learning  
✔ GenAI / LLMs  
✔ Prompt Engineering  
✔ RAG Systems  
✔ LangChain & Agents  
✔ AI Tools Ecosystem  

👉 Ask more specific topic
""")

# ─────────────────────────────
# 💼 JOBS ENGINE
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

    st.info("💡 Apply daily + build projects + improve GitHub")

# ─────────────────────────────
# 🎯 QUIZ SYSTEM
# ─────────────────────────────
elif mode == "🎯 Quiz":

    st.title("🎯 KronosAI Quiz Game")

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

        st.info("💡 Learn daily → become AI expert faster")

# ─────────────────────────────
# 📄 RESUME BUILDER (PRO ORDER)
# ─────────────────────────────
elif mode == "📄 Resume Builder":

    st.title("📄 ATS Resume Builder")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    summary = st.text_area("Professional Summary")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    experience = st.text_area("Internships / Experience")
    certs = st.text_area("Certifications")
    achievements = st.text_area("Achievements")
    tools = st.text_area("Tools & Technologies")
    links = st.text_area("GitHub / Portfolio Links")

    resume = f"""
========================
RESUME
========================

HEADER
Name: {name}
Email: {email}
Phone: {phone}

PROFESSIONAL SUMMARY
{summary}

EDUCATION
{education}

SKILLS
{skills}

PROJECTS
{projects}

INTERNSHIPS / EXPERIENCE
{experience}

CERTIFICATIONS
{certs}

ACHIEVEMENTS
{achievements}

TOOLS & TECHNOLOGIES
{tools}

LINKS
{links}
"""

    if st.button("Generate Resume"):
        st.text_area("ATS Resume", resume, height=500)

# ─────────────────────────────
# 🌐 PORTFOLIO BUILDER (STRUCTURED)
# ─────────────────────────────
elif mode == "🌐 Portfolio Builder":

    st.title("🌐 Portfolio Builder")

    name = st.text_input("Name")

    about = st.text_area("About Me")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    certs = st.text_area("Certifications")
    exp = st.text_area("Experience")
    resume_link = st.text_input("Resume Link")
    contact = st.text_input("Contact Info")

    portfolio = f"""
HOME / HERO
{name}

ABOUT ME
{about}

SKILLS
{skills}

PROJECTS (MOST IMPORTANT)
{projects}

CERTIFICATIONS
{certs}

EXPERIENCE
{exp}

RESUME DOWNLOAD
{resume_link}

CONTACT
{contact}
"""

    if st.button("Generate Portfolio"):
        st.text_area("Portfolio Structure", portfolio, height=500)