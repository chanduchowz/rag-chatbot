import streamlit as st
import random
import PyPDF2
from io import BytesIO
from reportlab.pdfgen import canvas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gtts import gTTS
import os

st.set_page_config(page_title="KronosAI SaaS 🚀", page_icon="🧠", layout="wide")

# ─────────────────────────────
# SIDEBAR (SAAS MODE)
# ─────────────────────────────
with st.sidebar:
    st.title("⚡ KronosAI SaaS")
    st.markdown("AI Career Platform")

    mode = st.radio(
        "Modules",
        [
            "💼 AI Job Feed",
            "📄 ATS Resume Builder",
            "🧠 AI Resume Checker",
            "🎤 Voice Interview Bot",
            "🌐 Portfolio Generator"
        ]
    )

# ─────────────────────────────
# 💼 AI JOB FEED (API READY STRUCTURE)
# ─────────────────────────────
if mode == "💼 AI Job Feed":

    st.title("💼 Smart AI Job Feed")

    role = st.selectbox("Role", ["Data Analyst", "AI Engineer", "GenAI Engineer", "ML Engineer"])
    exp = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])

    st.subheader("🔥 Recommended Jobs")

    jobs = {
        "Data Analyst": ["TCS DA Role", "Infosys Analyst", "Capgemini BI Analyst"],
        "AI Engineer": ["Google AI Engineer", "Microsoft AI Role", "IBM AI Role"],
        "GenAI Engineer": ["OpenAI Startup Roles", "LangChain Engineer Jobs"],
        "ML Engineer": ["Amazon ML Role", "Meta ML Engineer"]
    }

    for j in jobs[role]:
        st.success(j)

    st.markdown("👉 Apply via LinkedIn / Naukri APIs (integration ready)")

# ─────────────────────────────
# 📄 ATS RESUME BUILDER
# ─────────────────────────────
elif mode == "📄 ATS Resume Builder":

    st.title("📄 ATS Resume Builder")

    name = st.text_input("Name")
    email = st.text_input("Email")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    resume_text = f"""
NAME: {name}
EMAIL: {email}

SKILLS:
{skills}

PROJECTS:
{projects}
"""

    if st.button("Generate Resume"):
        st.text_area("ATS Resume", resume_text, height=300)

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

        pdf = create_pdf(resume_text)
        st.download_button("Download PDF", pdf, file_name="resume.pdf")

# ─────────────────────────────
# 🧠 AI RESUME CHECKER (REAL SCORING)
# ─────────────────────────────
elif mode == "🧠 AI Resume Checker":

    st.title("🧠 AI ATS Score Engine")

    uploaded = st.file_uploader("Upload Resume PDF", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    def extract(file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for p in reader.pages:
            text += p.extract_text()
        return text

    def calculate_score(resume, job):
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume, job])
        score = cosine_similarity(vectors[0], vectors[1])[0][0]
        return round(score * 100, 2)

    if uploaded:

        resume_text = extract(uploaded)

        if st.button("Check ATS Score"):

            if len(job_desc) < 10:
                st.error("Add Job Description")
            else:
                score = calculate_score(resume_text, job_desc)

                st.success(f"ATS Match Score: {score}/100")

                if score < 50:
                    st.warning("Low Match - Improve keywords")
                elif score < 75:
                    st.info("Good Match - Improve projects")
                else:
                    st.success("Excellent Match - Ready to apply")

# ─────────────────────────────
# 🎤 VOICE INTERVIEW BOT (TEXT + SPEECH)
# ─────────────────────────────
elif mode == "🎤 Voice Interview Bot":

    st.title("🎤 AI Voice Interviewer")

    questions = [
        "Explain RAG in AI",
        "What is overfitting?",
        "Explain your project",
        "What is GenAI?",
        "What is vector database?"
    ]

    q = random.choice(questions)

    st.warning(f"Question: {q}")

    if st.button("🔊 Speak Question"):

        tts = gTTS(q)
        tts.save("q.mp3")
        audio_file = open("q.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

    ans = st.text_area("Your Answer")

    if st.button("Evaluate Answer"):

        if len(ans) < 30:
            st.error("Too short answer")
        else:
            st.success("Good Answer Structure")

            st.info("""
Improve:
✔ Add example  
✔ Add technical terms  
✔ Structure: Definition → Working → Example  
""")

# ─────────────────────────────
# 🌐 PORTFOLIO GENERATOR (PRO SAAS)
# ─────────────────────────────
elif mode == "🌐 Portfolio Generator":

    st.title("🌐 AI Portfolio Builder")

    name = st.text_input("Name")
    role = st.selectbox("Role", ["Data Analyst", "AI Engineer", "ML Engineer", "GenAI Engineer"])

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