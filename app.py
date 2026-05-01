import streamlit as st
import random
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
# AI KNOWLEDGE BASE
# ─────────────────────────────
AI_SYLLABUS = {
    "python": "Python is used in AI, ML, automation and data science.",
    "ai": "AI is simulation of human intelligence.",
    "ml": "Machine Learning learns patterns from data.",
    "dl": "Deep Learning uses neural networks.",
    "genai": "Generative AI creates text, images, code.",
    "rag": "RAG = Retrieval + LLM generation system.",
    "llm": "LLMs like GPT are transformer-based models."
}

# ─────────────────────────────
# 🧠 AI TUTOR
# ─────────────────────────────
if mode == "🧠 AI Tutor":

    st.title("🧠 KronosAI Tutor")

    q = st.text_input("Ask anything")

    if q:
        found = False

        for k in AI_SYLLABUS:
            if k in q.lower():
                st.success(AI_SYLLABUS[k])
                found = True
                break

        if not found:
            st.info("Ask about AI, ML, DL, GenAI, RAG, LLM, Python")

# ─────────────────────────────
# 💼 JOB ENGINE
# ─────────────────────────────
elif mode == "💼 Jobs":

    st.title("💼 Job Engine")

    role = st.selectbox("Role", [
        "Data Analyst",
        "AI Engineer",
        "ML Engineer",
        "Python Developer"
    ])

    exp = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])

    jobs = {
        "Fresher": ["TCS Trainee", "Infosys Analyst", "Wipro Intern"],
        "1-3 Years": ["Accenture AI Engineer", "Amazon Analyst"],
        "3+ Years": ["Google Engineer", "Microsoft Data Scientist"]
    }

    st.subheader("🔥 Recommended Jobs")

    for j in jobs[exp]:
        st.success(j)

# ─────────────────────────────
# 🎯 QUIZ (FIXED MCQ SYSTEM)
# ─────────────────────────────
elif mode == "🎯 Quiz":

    st.title("🎯 KronosAI MCQ Quiz Game")

    quizzes = [
        {
            "q": "What is Artificial Intelligence?",
            "options": [
                "Machines simulating human intelligence",
                "A programming language",
                "A database system",
                "A web browser"
            ],
            "ans": "Machines simulating human intelligence"
        },
        {
            "q": "What is Machine Learning?",
            "options": [
                "Learning from data",
                "Manual coding",
                "Operating system",
                "Cloud storage"
            ],
            "ans": "Learning from data"
        },
        {
            "q": "What is RAG?",
            "options": [
                "Retrieval + LLM system",
                "Random AI generator",
                "Robot automation game",
                "Real analytics group"
            ],
            "ans": "Retrieval + LLM system"
        },
        {
            "q": "What is LLM?",
            "options": [
                "Large Language Model",
                "Logical Learning Machine",
                "Light Layer Model",
                "Long Learning Method"
            ],
            "ans": "Large Language Model"
        }
    ]

    qz = random.choice(quizzes)

    st.subheader(qz["q"])

    choice = st.radio("Select answer:", qz["options"], index=None)

    if st.button("Submit Answer"):

        if choice is None:
            st.warning("Please select an option")
        elif choice == qz["ans"]:
            st.success("✅ Correct Answer 🎉")
        else:
            st.error(f"❌ Wrong Answer\nCorrect: {qz['ans']}")

    st.info("💡 Practice daily quizzes to improve AI skills")

# ─────────────────────────────
# 📄 RESUME BUILDER (ATS + ANALYSIS)
# ─────────────────────────────
elif mode == "📄 Resume Builder":

    st.title("📄 ATS Resume Analyzer")

    uploaded_file = st.file_uploader("Upload Resume (PDF - max 5MB)", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    def extract_text(file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    def score(resume, job):
        tfidf = TfidfVectorizer()
        vectors = tfidf.fit_transform([resume, job])
        return round(cosine_similarity(vectors[0], vectors[1])[0][0] * 100, 2)

    if uploaded_file:

        if uploaded_file.size > 5 * 1024 * 1024:
            st.error("File too large (Max 5MB)")
        else:

            resume_text = extract_text(uploaded_file)

            if st.button("Analyze Resume"):

                if len(job_desc) < 10:
                    st.error("Paste job description")
                else:

                    ats = score(resume_text, job_desc)

                    st.success(f"ATS Score: {ats}/100")

                    if ats < 50:
                        st.warning("Low match → Add keywords & projects")
                    elif ats < 75:
                        st.info("Good match → Improve skills section")
                    else:
                        st.success("Excellent match → Ready to apply")

# ─────────────────────────────
# 🌐 PORTFOLIO BUILDER
# ─────────────────────────────
elif mode == "🌐 Portfolio Builder":

    st.title("🌐 Portfolio Builder")

    name = st.text_input("Name")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    if st.button("Generate Portfolio"):

        portfolio = f"""
HOME
{name}

ABOUT
AI/ML Enthusiast

SKILLS
{skills}

PROJECTS (IMPORTANT)
{projects}

CONTACT
Available for AI / ML roles
"""

        st.text_area("Portfolio", portfolio, height=400)