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
            "💬 AI Tutor",
            "💼 Job Engine",
            "🎯 AI Quiz Game",
            "📄 Resume Builder",
            "🌐 Portfolio Builder"
        ]
    )

# ─────────────────────────────
# AI DOMAIN KNOWLEDGE ENGINE
# ─────────────────────────────
AI_KNOWLEDGE = {
    "ai": "Artificial Intelligence is the simulation of human intelligence in machines.",
    "ml": "Machine Learning is AI that learns patterns from data.",
    "dl": "Deep Learning uses neural networks with many layers.",
    "genai": "Generative AI creates text, images, code using models like GPT.",
    "llm": "Large Language Models are transformer-based models trained on massive text.",
    "rag": "Retrieval Augmented Generation combines search + LLM generation.",
    "agent": "AI Agents can plan, think, and execute multi-step tasks.",
    "transformer": "Transformer is architecture behind GPT models."
}

# ─────────────────────────────
# 💬 AI TUTOR (ACCURATE + MULTI DOMAIN)
# ─────────────────────────────
if mode == "💬 AI Tutor":

    st.title("💬 KronosAI Tutor")

    q = st.text_input("Ask anything (AI / ML / DL / GenAI / Careers)")

    if q:

        key = None
        for k in AI_KNOWLEDGE:
            if k in q.lower():
                key = k
                break

        if key:
            st.success(AI_KNOWLEDGE[key])
        else:
            st.info("""
I can explain:
✔ AI / ML / DL  
✔ GenAI / LLMs / RAG / Agents  
✔ Career guidance  
✔ Projects / interviews  

Please ask more specific question.
""")

# ─────────────────────────────
# 💼 JOB ENGINE (ALL ROLES + EXPERIENCE)
# ─────────────────────────────
elif mode == "💼 Job Engine":

    st.title("💼 Smart Job Engine")

    role = st.selectbox("Role", [
        "Data Analyst",
        "Software Developer",
        "AI Engineer",
        "ML Engineer",
        "GenAI Engineer",
        "Business Analyst"
    ])

    exp = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])

    jobs = {
        "Fresher": [
            "TCS - Graduate Trainee",
            "Infosys - Analyst Trainee",
            "Wipro - Developer Intern",
            "Capgemini - Entry Role"
        ],
        "1-3 Years": [
            "Accenture - Analyst",
            "Amazon - SDE",
            "IBM - AI Engineer",
            "Cognizant - Developer"
        ],
        "3+ Years": [
            "Google - Senior Engineer",
            "Microsoft - Data Scientist",
            "Meta - ML Engineer",
            "Startup - AI Lead"
        ]
    }

    st.subheader(f"🔥 Jobs for {role} ({exp})")

    for j in jobs[exp]:
        st.success(j)

# ─────────────────────────────
# 🎯 AI QUIZ GAME (LEARNING STYLE)
# ─────────────────────────────
elif mode == "🎯 AI Quiz Game":

    st.title("🎯 KronosAI Learning Game")

    quizzes = [
        ("What is AI?", "Simulation of human intelligence"),
        ("What is ML?", "Learning from data"),
        ("What is DL?", "Neural networks with layers"),
        ("What is GenAI?", "Creates content like text/images"),
        ("What is LLM?", "Large language model like GPT"),
    ]

    q, ans = random.choice(quizzes)

    st.subheader(q)

    user = st.text_input("Your Answer")

    if st.button("Check"):

        if ans.lower() in user.lower():
            st.success("Correct 🎉")
        else:
            st.error(f"Wrong ❌ Answer: {ans}")

# ─────────────────────────────
# 📄 RESUME BUILDER (PRO FORMAT ORDER)
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
    internship = st.text_area("Internships / Experience")
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
{internship}

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
# 🌐 PORTFOLIO BUILDER (PRO ORDER STRUCTURE)
# ─────────────────────────────
elif mode == "🌐 Portfolio Builder":

    st.title("🌐 AI Portfolio Builder")

    name = st.text_input("Name")

    about = st.text_area("About Me")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects (MOST IMPORTANT)")
    certs = st.text_area("Certifications")
    exp = st.text_area("Experience")
    resume_link = st.text_input("Resume Download Link")
    contact = st.text_input("Contact Info")

    portfolio = f"""
HOME / HERO
{name} - AI/ML Enthusiast

ABOUT ME
{about}

SKILLS
{skills}

PROJECTS
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