import streamlit as st
import random
import PyPDF2
from io import BytesIO
from reportlab.pdfgen import canvas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gtts import gTTS
import os

# ─────────────────────────────
# CONFIG
# ─────────────────────────────
st.set_page_config(page_title="KronosAI SaaS 🚀", page_icon="🧠", layout="wide")

# ─────────────────────────────
# SIDEBAR
# ─────────────────────────────
with st.sidebar:
    st.title("⚡ KronosAI SaaS")

    mode = st.radio(
        "Select Module",
        [
            "💬 AI Tutor",
            "💼 AI Job Feed",
            "📄 ATS Resume Builder",
            "🧠 AI Resume Checker",
            "🎤 Voice Interview Bot",
            "🌐 Portfolio Generator"
        ]
    )

# ─────────────────────────────
# 💬 AI TUTOR (SAFE VERSION - NO FAISS ERROR)
# ─────────────────────────────
if mode == "💬 AI Tutor":

    st.title("💬 KronosAI Tutor")

    st.info("Ask anything about AI / ML / GenAI / RAG / Careers")

    q = st.text_input("Your Question")

    if q:

        if "rag" in q.lower():
            st.success("RAG = Retrieval Augmented Generation (search + LLM combination)")
        elif "genai" in q.lower():
            st.success("GenAI = AI that generates content like text, images, code")
        else:
            st.info("AI Answer: This is a concept in AI/ML. Learn step by step from basics → advanced.")

# ─────────────────────────────
# 💼 JOB FEED
# ─────────────────────────────
elif mode == "💼 AI Job Feed":

    st.title("💼 AI Job Engine")

    role = st.selectbox("Role", ["Data Analyst", "AI Engineer", "GenAI Engineer", "ML Engineer"])

    jobs = {
        "Data Analyst": ["TCS Analyst", "Infosys DA", "Capgemini BI Role"],
        "AI Engineer": ["Google AI Engineer", "Microsoft AI Role"],
        "GenAI Engineer": ["OpenAI Startup Roles", "LangChain Jobs"],
        "ML Engineer": ["Amazon ML Role", "Meta ML Engineer"]
    }

    st.subheader("🔥 Jobs")
    for j in jobs[role]:
        st.success(j)

    st.info("Apply via LinkedIn / Naukri")

# ─────────────────────────────
# 📄 ATS RESUME BUILDER
# ─────────────────────────────
elif mode == "📄 ATS Resume Builder":

    st.title("📄 Resume Builder")

    name = st.text_input("Name")
    email = st.text_input("Email")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    resume = f"""
NAME: {name}
EMAIL: {email}

SKILLS:
{skills}

PROJECTS:
{projects}
"""

    if st.button("Generate Resume"):
        st.text_area("ATS Resume", resume, height=300)

        def create_pdf(text):
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            y = 800
            for line in text.split("\n"):
                p.drawString(50, y, line[:100])
                y -= 15
            p.save()
            buffer.seek(0)
            return buffer

        pdf = create_pdf(resume)
        st.download_button("Download PDF", pdf, file_name="resume.pdf")

# ─────────────────────────────
# 🧠 AI RESUME CHECKER
# ─────────────────────────────
elif mode == "🧠 AI Resume Checker":

    st.title("🧠 ATS Score Checker")

    uploaded = st.file_uploader("Upload Resume PDF", type=["pdf"])
    job = st.text_area("Paste Job Description")

    def extract(file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for p in reader.pages:
            text += p.extract_text()
        return text

    def score(resume, job):
        vectorizer = TfidfVectorizer()
        v = vectorizer.fit_transform([resume, job])
        return round(cosine_similarity(v[0], v[1])[0][0] * 100, 2)

    if uploaded:

        if uploaded.size > 5 * 1024 * 1024:
            st.error("Max 5MB allowed")
        else:
            resume_text = extract(uploaded)

            if st.button("Check Score"):

                s = score(resume_text, job)

                st.success(f"ATS Score: {s}/100")

                if s < 50:
                    st.warning("Improve keywords")
                elif s < 75:
                    st.info("Good resume")
                else:
                    st.success("Strong resume")

# ─────────────────────────────
# 🎤 VOICE INTERVIEW BOT
# ─────────────────────────────
elif mode == "🎤 Voice Interview Bot":

    st.title("🎤 AI Interview Bot")

    q = random.choice([
        "Explain RAG",
        "What is ML?",
        "Explain GenAI",
        "What is overfitting?"
    ])

    st.warning(q)

    if st.button("🔊 Speak Question"):
        tts = gTTS(q)
        tts.save("q.mp3")
        st.audio("q.mp3")

    ans = st.text_area("Your Answer")

    if st.button("Evaluate"):

        if len(ans) < 20:
            st.error("Too short")
        else:
            st.success("Good Answer")
            st.info("Add example + structure + keywords")

# ─────────────────────────────
# 🌐 PORTFOLIO GENERATOR
# ─────────────────────────────
elif mode == "🌐 Portfolio Generator":

    st.title("🌐 Portfolio Builder")

    name = st.text_input("Name")
    role = st.selectbox("Role", ["Data Analyst", "AI Engineer", "ML Engineer"])

    about = st.text_area("About")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    github = st.text_input("GitHub")
    linkedin = st.text_input("LinkedIn")

    if st.button("Generate Portfolio"):

        html = f"""
        <html>
        <body>
        <h1>{name}</h1>
        <h3>{role}</h3>

        <h2>About</h2>
        <p>{about}</p>

        <h2>Skills</h2>
        <p>{skills}</p>

        <h2>Projects</h2>
        <p>{projects}</p>

        <h2>Links</h2>
        <p>{github}</p>
        <p>{linkedin}</p>
        </body>
        </html>
        """

        st.download_button("Download Portfolio", html, file_name="portfolio.html")