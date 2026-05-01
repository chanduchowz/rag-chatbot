import streamlit as st
import random
import PyPDF2

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
# AI KNOWLEDGE
# ─────────────────────────────
AI_KNOWLEDGE = {
    "ai": "AI simulates human intelligence.",
    "ml": "ML learns patterns from data.",
    "dl": "DL uses neural networks.",
    "genai": "Generates text/images/code.",
    "llm": "Large Language Models like GPT.",
    "rag": "Search + AI generation system."
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
            st.info("Ask AI / ML / DL / GenAI / RAG / LLM")

# ─────────────────────────────
# 💼 JOBS
# ─────────────────────────────
elif mode == "💼 Jobs":

    st.title("💼 AI Job Engine")

    role = st.selectbox("Role", ["AI Engineer", "ML Engineer", "Data Analyst", "Python Dev"])
    exp = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])

    jobs = {
        "Fresher": ["TCS", "Infosys", "Wipro"],
        "1-3 Years": ["Accenture", "Amazon", "IBM"],
        "3+ Years": ["Google", "Microsoft", "Meta"]
    }

    st.subheader("🔥 Jobs")

    for j in jobs[exp]:
        st.success(j)

# ─────────────────────────────
# 🎯 QUIZ GAME (ZIGZAG OPTIONS + NEXT BUTTON)
# ─────────────────────────────
elif mode == "🎯 Quiz Game":

    st.title("🎯 KronosAI Quiz Game (Pro Mode)")

    # INIT SESSION
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False

    questions = [
        ("What is AI?", "Simulation of intelligence"),
        ("What is ML?", "Learning from data"),
        ("What is DL?", "Neural networks"),
        ("What is GenAI?", "Creates content"),
        ("What is LLM?", "Large language model"),
        ("What is RAG?", "Search + AI system"),
        ("Python is used for?", "AI development"),
        ("Overfitting means?", "Memorizing data")
    ]

    # expand to 100+
    while len(questions) < 100:
        questions.append(random.choice(questions))

    idx = st.session_state.q_index % len(questions)

    q, ans = questions[idx]

    st.subheader(q)

    # ─────────────────────────────
    # CREATE ZIGZAG OPTIONS (SHUFFLE EVERY TIME)
    # ─────────────────────────────
    wrong_pool = [
        "Database system",
        "Operating system",
        "Web browser",
        "Game engine",
        "File system",
        "Cloud storage",
        "Random output"
    ]

    options = [ans] + random.sample(wrong_pool, 3)
    random.shuffle(options)   # 🔥 zig-zag order change

    selected = st.radio("Choose answer:", options, key=str(idx))

    # ─────────────────────────────
    # CHECK ANSWER
    # ─────────────────────────────
    if not st.session_state.answered:

        if st.button("Submit Answer"):

            st.session_state.answered = True

            if selected == ans:
                st.success("Correct 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Wrong ❌ Correct: {ans}")

            st.info(f"Score: {st.session_state.score}")

    # ─────────────────────────────
    # NEXT QUESTION BUTTON
    # ─────────────────────────────
    if st.session_state.answered:

        if st.button("➡ Next Question"):

            st.session_state.q_index += 1
            st.session_state.answered = False
            st.rerun()

# ─────────────────────────────
# 📄 RESUME ANALYZER
# ─────────────────────────────
elif mode == "📄 Resume Analyzer":

    st.title("📄 Resume Analyzer")

    file = st.file_uploader("Upload PDF (Max 5MB)", type=["pdf"])
    job = st.text_area("Job Description")

    def extract(file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for p in reader.pages:
            text += p.extract_text() or ""
        return text

    if file:

        if file.size > 5 * 1024 * 1024:
            st.error("Max 5MB allowed")
        else:
            resume = extract(file)

            if st.button("Analyze"):

                match = len(set(resume.lower().split()) & set(job.lower().split()))
                score = min(match * 3, 100)

                st.success(f"ATS Score: {score}/100")

                st.subheader("Improved Resume")

                improved = f"""
KEYWORDS MATCHED:
{list(set(resume.split()) & set(job.split()))}

SUGGESTIONS:
- Add missing keywords
- Improve project impact
- Add numbers (metrics)

ORIGINAL PREVIEW:
{resume[:800]}
"""

                st.text_area("Improved Resume", improved, height=400)

# ─────────────────────────────
# 🌐 PORTFOLIO BUILDER
# ─────────────────────────────
elif mode == "🌐 Portfolio Builder":

    st.title("🌐 Portfolio Builder")

    name = st.text_input("Name")
    about = st.text_area("About")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    if st.button("Generate"):

        html = f"""
        <html>
        <body>
        <h1>{name}</h1>
        <h2>About</h2><p>{about}</p>
        <h2>Skills</h2><p>{skills}</p>
        <h2>Projects</h2><p>{projects}</p>
        </body>
        </html>
        """

        st.download_button("Download Portfolio", html, file_name="portfolio.html")