import streamlit as st
import random
import PyPDF2

st.set_page_config(page_title="KronosAI 🚀", page_icon="🧠", layout="wide")

# ─────────────────────────────
# SIDEBAR (AI TUTOR REMOVED)
# ─────────────────────────────
with st.sidebar:
    st.title("⚡ KronosAI")

    mode = st.radio(
        "Choose Mode",
        [
            "💼 Jobs",
            "🎯 Quiz Game",
            "📄 Resume Builder",
            "📊 Resume Analyzer",
            "🌐 Portfolio Builder"
        ]
    )

# ─────────────────────────────
# 💼 JOB ENGINE (WITH APPLY LINKS)
# ─────────────────────────────
elif mode == "💼 Jobs":

    st.title("💼 AI Job Engine - Apply Directly")

    role = st.selectbox("Role", ["AI Engineer", "ML Engineer", "Data Analyst", "Python Dev"])
    exp = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])

    jobs = {
        "Fresher": [
            ("TCS", "https://www.tcs.com/careers"),
            ("Infosys", "https://www.infosys.com/careers"),
            ("Wipro", "https://careers.wipro.com")
        ],
        "1-3 Years": [
            ("Accenture", "https://www.accenture.com/in-en/careers"),
            ("Amazon", "https://www.amazon.jobs"),
            ("IBM", "https://www.ibm.com/employment")
        ],
        "3+ Years": [
            ("Google", "https://careers.google.com"),
            ("Microsoft", "https://careers.microsoft.com"),
            ("Meta", "https://www.metacareers.com")
        ]
    }

    st.subheader("🔥 Click to Apply")

    for company, link in jobs[exp]:
        st.markdown(f"### 🏢 {company}")
        st.markdown(f"[👉 Apply Here]({link})")
        st.write("---")

# ─────────────────────────────
# 🎯 QUIZ GAME
# ─────────────────────────────
elif mode == "🎯 Quiz Game":

    st.title("🎯 KronosAI Quiz Game")

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
        ("Python used for?", "AI development"),
        ("Overfitting means?", "Memorizing data")
    ]

    while len(questions) < 100:
        questions.append(random.choice(questions))

    idx = st.session_state.q_index % len(questions)
    q, ans = questions[idx]

    st.subheader(q)

    wrongs = ["Database", "OS", "Cloud", "Game Engine", "Browser", "Compiler"]

    options = [ans] + random.sample(wrongs, 3)
    random.shuffle(options)

    selected = st.radio("Choose answer", options, key=str(idx))

    if not st.session_state.answered:

        if st.button("Submit"):

            st.session_state.answered = True

            if selected == ans:
                st.success("Correct 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Wrong ❌ Correct: {ans}")

            st.info(f"Score: {st.session_state.score}")

    if st.session_state.answered:

        if st.button("Next Question ➡"):

            st.session_state.q_index += 1
            st.session_state.answered = False
            st.rerun()

# ─────────────────────────────
# 📄 RESUME BUILDER
# ─────────────────────────────
elif mode == "📄 Resume Builder":

    st.title("📄 ATS Resume Builder (Manual)")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    location = st.text_input("Location")

    summary = st.text_area("Professional Summary")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    experience = st.text_area("Experience")
    certifications = st.text_area("Certifications")
    achievements = st.text_area("Achievements")
    tools = st.text_area("Tools & Technologies")
    links = st.text_area("GitHub / Portfolio Links")

    if st.button("Generate ATS Resume"):

        resume = f"""
========================
        ATS RESUME
========================

Name: {name}
Email: {email}
Phone: {phone}
Location: {location}

SUMMARY
{summary}

EDUCATION
{education}

SKILLS
{skills}

PROJECTS
{projects}

EXPERIENCE
{experience}

CERTIFICATIONS
{certifications}

ACHIEVEMENTS
{achievements}

TOOLS
{tools}

LINKS
{links}

========================
"""

        st.text_area("Generated Resume", resume, height=600)
        st.success("Resume Generated 🎉")

# ─────────────────────────────
# 📊 RESUME ANALYZER
# ─────────────────────────────
elif mode == "📊 Resume Analyzer":

    st.title("📊 Resume Analyzer")

    uploaded = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    def extract_text(file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for p in reader.pages:
            text += p.extract_text() or ""
        return text

    if uploaded:

        if uploaded.size > 5 * 1024 * 1024:
            st.error("File too large")
        else:

            resume_text = extract_text(uploaded)

            if st.button("Analyze Resume"):

                resume_words = set(resume_text.lower().split())
                job_words = set(job_desc.lower().split())

                match = resume_words & job_words
                score = min(len(match) * 3, 100)

                st.success(f"ATS Score: {score}/100")
                st.write(list(match))

# ─────────────────────────────
# 🌐 PORTFOLIO BUILDER
# ─────────────────────────────
elif mode == "🌐 Portfolio Builder":

    st.title("🌐 Portfolio Builder")

    name = st.text_input("Name")
    about = st.text_area("About")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    certs = st.text_area("Certifications")
    exp = st.text_area("Experience")
    resume_link = st.text_input("Resume Link")
    contact = st.text_input("Contact")

    if st.button("Generate Portfolio"):

        html = f"""
        <html>
        <body>
        <h1>{name}</h1>
        <p>{about}</p>
        <h2>Skills</h2>
        <p>{skills}</p>
        <h2>Projects</h2>
        <p>{projects}</p>
        <h2>Certifications</h2>
        <p>{certs}</p>
        <h2>Experience</h2>
        <p>{exp}</p>
        <h2>Resume</h2>
        <p>{resume_link}</p>
        <h2>Contact</h2>
        <p>{contact}</p>
        </body>
        </html>
        """

        st.success("Portfolio Generated (HTML Ready)")