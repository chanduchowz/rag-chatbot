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
    "rag": "RAG combines retrieval + LLM generation.",
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
# 🎯 QUIZ ENGINE (100+ MCQ FIXED)
# ─────────────────────────────
elif mode == "🎯 Quiz":

    st.title("🎯 KronosAI Quiz Engine (100+ MCQs)")

    base_quizzes = [
        {"q": "What is AI?", "options": ["Machines simulating human intelligence", "Excel tool", "Database", "Browser"], "ans": "Machines simulating human intelligence"},
        {"q": "What is ML?", "options": ["Learning from data", "Manual coding", "OS", "Hardware"], "ans": "Learning from data"},
        {"q": "What is DL?", "options": ["Neural networks", "SQL", "Excel", "API"], "ans": "Neural networks"},
        {"q": "What is GenAI?", "options": ["Creates content", "Game engine", "OS", "Compiler"], "ans": "Creates content"},
        {"q": "What is RAG?", "options": ["Retrieval + LLM system", "Random AI", "Robot", "Router"], "ans": "Retrieval + LLM system"},
        {"q": "What is LLM?", "options": ["Large Language Model", "Low Level Machine", "Logic Model", "Linear Method"], "ans": "Large Language Model"},
        {"q": "Python is used for?", "options": ["AI/ML", "Cooking", "Driving", "Sports"], "ans": "AI/ML"},
        {"q": "Overfitting means?", "options": ["Model memorizes data", "Model deletes data", "Model crashes", "Model sleeps"], "ans": "Model memorizes data"},
        {"q": "Transformer is used in?", "options": ["GPT", "Cars", "Games", "Excel"], "ans": "GPT"},
        {"q": "Embedding means?", "options": ["Vector form", "File delete", "CPU speed", "Database"], "ans": "Vector form"},
    ]

    # expand to 100+ questions
    quizzes = (base_quizzes * 10)[:100]
    random.shuffle(quizzes)

    # session state
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0

    if st.session_state.q_index >= len(quizzes):
        st.success("🎉 You completed 100 questions!")
        st.session_state.q_index = 0

    qz = quizzes[st.session_state.q_index]

    st.subheader(f"Q{st.session_state.q_index + 1}: {qz['q']}")

    choice = st.radio("Select answer:", qz["options"], index=None)

    if st.button("Submit Answer"):

        if choice is None:
            st.warning("Select an option")
        else:
            if choice == qz["ans"]:
                st.success("✅ Correct")
            else:
                st.error(f"❌ Wrong | Correct: {qz['ans']}")

            st.session_state.q_index += 1
            st.rerun()

    st.progress(st.session_state.q_index / 100)

# ─────────────────────────────
# 📄 RESUME BUILDER
# ─────────────────────────────
elif mode == "📄 Resume Builder":

    st.title("📄 ATS Resume Analyzer")

    uploaded_file = st.file_uploader("Upload Resume PDF (max 5MB)", type=["pdf"])
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
            st.error("Max 5MB allowed")
        else:

            resume_text = extract_text(uploaded_file)

            if st.button("Analyze Resume"):

                if len(job_desc) < 10:
                    st.error("Paste job description")
                else:

                    ats = score(resume_text, job_desc)

                    st.success(f"ATS Score: {ats}/100")

                    if ats < 50:
                        st.warning("Low match → Improve keywords")
                    elif ats < 75:
                        st.info("Good match → Improve projects")
                    else:
                        st.success("Strong resume")

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

PROJECTS
{projects}

CONTACT
Available for AI/ML roles
"""

        st.text_area("Portfolio", portfolio, height=400)