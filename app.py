import streamlit as st
import random
import PyPDF2
from io import BytesIO

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
            "🎯 Quiz Game",
            "📄 Resume Analyzer",
            "🌐 Portfolio Builder"
        ]
    )

# ─────────────────────────────
# AI KNOWLEDGE ENGINE
# ─────────────────────────────
AI_KNOWLEDGE = {
    "ai": "Artificial Intelligence simulates human intelligence.",
    "ml": "Machine Learning learns patterns from data.",
    "dl": "Deep Learning uses neural networks.",
    "genai": "Generative AI creates text, images, code.",
    "llm": "Large Language Models like GPT.",
    "rag": "Retrieval Augmented Generation = search + AI."
}

# ─────────────────────────────
# 🧠 AI TUTOR
# ─────────────────────────────
if mode == "🧠 AI Tutor":

    st.title("🧠 KronosAI Tutor")

    q = st.text_input("Ask anything")

    if q:
        found = False
        for k, v in AI_KNOWLEDGE.items():
            if k in q.lower():
                st.success(v)
                found = True
                break

        if not found:
            st.info("Ask AI / ML / DL / GenAI / RAG / LLM related questions")

# ─────────────────────────────
# 💼 JOB ENGINE
# ─────────────────────────────
elif mode == "💼 Jobs":

    st.title("💼 AI Job Engine")

    role = st.selectbox("Role", [
        "Data Analyst", "AI Engineer", "ML Engineer", "GenAI Engineer", "Python Developer"
    ])

    exp = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])

    jobs = {
        "Fresher": ["TCS Analyst", "Infosys Trainee", "Wipro Developer"],
        "1-3 Years": ["Accenture AI Engineer", "Amazon Analyst", "IBM ML Engineer"],
        "3+ Years": ["Google Engineer", "Microsoft Data Scientist", "Meta AI Engineer"]
    }

    st.subheader("🔥 Jobs for You")

    for j in jobs[exp]:
        st.success(j)

# ─────────────────────────────
# 🎯 QUIZ GAME (100+ MCQ + UNLIMITED)
# ─────────────────────────────
elif mode == "🎯 Quiz Game":

    st.title("🎯 KronosAI Quiz Game (MCQ + Infinite)")

    # 100+ QUESTIONS BANK
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    questions = [
        ("What is AI?", ["Simulation of intelligence", "Excel tool", "Database", "OS"], 0),
        ("What is ML?", ["Learning from data", "Coding style", "Cloud system", "UI design"], 0),
        ("What is DL?", ["Neural networks", "SQL query", "API", "Storage"], 0),
        ("What is GenAI?", ["Creates content", "Deletes files", "Networking", "Browser"], 0),
        ("What is LLM?", ["Large Language Model", "Linux system", "Logic Layer Module", "None"], 0),
        ("What is RAG?", ["Search + AI", "Game engine", "Database", "Compiler"], 0),
        ("Python used for?", ["AI development", "Only gaming", "Hardware", "UI only"], 0),
        ("Overfitting means?", ["Memorizing data", "Fast training", "Cloud error", "API call"], 0),
        ("Transformer used in?", ["GPT models", "Excel", "OS", "Photoshop"], 0),
        ("ChatGPT is?", ["LLM", "Database", "Game", "Compiler"], 0)
    ]

    # LOOP FOR 100+ (AUTO EXPAND)
    while len(questions) < 100:
        base = random.choice(questions)
        questions.append(base)

    index = st.session_state.quiz_index % len(questions)

    q, options, correct = questions[index]

    st.subheader(q)

    choice = st.radio("Choose answer", options, key=index)

    if st.button("Submit Answer"):

        if options.index(choice) == correct:
            st.success("Correct 🎉")
            st.session_state.score += 1
        else:
            st.error(f"Wrong ❌ Correct: {options[correct]}")

        st.info(f"Score: {st.session_state.score}")

        st.session_state.quiz_index += 1

# ─────────────────────────────
# 📄 RESUME ANALYZER (UPLOAD + AI IMPROVEMENT)
# ─────────────────────────────
elif mode == "📄 Resume Analyzer":

    st.title("📄 AI Resume Analyzer + Optimizer")

    uploaded = st.file_uploader("Upload Resume (PDF, max 5MB)", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    def extract_pdf(file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    if uploaded:

        if uploaded.size > 5 * 1024 * 1024:
            st.error("File exceeds 5MB limit")
        else:
            resume_text = extract_pdf(uploaded)

            st.success("Resume Uploaded")

            if st.button("Analyze Resume"):

                common_words = set(resume_text.lower().split()) & set(job_desc.lower().split())

                score = len(common_words) * 2

                st.success(f"ATS Score: {min(score, 100)}/100")

                st.info("✔ Missing keywords will reduce selection chances")

                st.subheader("🚀 Improved ATS Resume")

                improved = f"""
ATS OPTIMIZED RESUME

Key Skills Matched:
{', '.join(list(common_words))}

Recommendation:
- Add missing keywords from job description
- Add measurable achievements
- Add tools like Python, SQL, Power BI, ML

Original Resume:
{resume_text[:1000]}
"""

                st.text_area("Improved Resume", improved, height=400)

# ─────────────────────────────
# 🌐 PORTFOLIO BUILDER
# ─────────────────────────────
elif mode == "🌐 Portfolio Builder":

    st.title("🌐 Portfolio Generator")

    name = st.text_input("Name")
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