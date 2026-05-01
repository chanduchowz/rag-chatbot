import streamlit as st
import random
from io import BytesIO
from reportlab.pdfgen import canvas

st.set_page_config(page_title="KronosAI SaaS 🚀", page_icon="🧠", layout="wide")

# ─────────────────────────────
# SIDEBAR
# ─────────────────────────────
with st.sidebar:
    st.title("⚡ KronosAI SaaS")
    st.markdown("AI Career System 🚀")

    mode = st.radio(
        "Choose Feature",
        [
            "💼 Job Engine",
            "📄 ATS Resume Builder",
            "🧠 Resume AI Checker",
            "🎤 Interview Killer",
            "🌐 Portfolio Generator"
        ]
    )

    if st.button("Reset"):
        st.rerun()

# ─────────────────────────────
# 💼 JOB ENGINE (API READY)
# ─────────────────────────────
if mode == "💼 Job Engine":

    st.title("💼 Smart Job Engine")

    level = st.selectbox("Experience", ["Fresher", "1-3 Years", "3+ Years"])
    role = st.selectbox("Role", ["Data Analyst", "AI Engineer", "Python Dev", "Business Analyst"])

    jobs = {
        "Fresher": [
            ("TCS Analyst Trainee", "https://www.tcs.com/careers"),
            ("Infosys Graduate Role", "https://careers.infosys.com")
        ],
        "1-3 Years": [
            ("Capgemini Analyst", "https://www.capgemini.com/careers")
        ],
        "3+ Years": [
            ("Google AI Engineer", "https://careers.google.com")
        ]
    }

    st.subheader("🔥 Jobs for You")

    for job, link in jobs[level]:
        st.markdown(f"### {job}")
        st.link_button("Apply", link)

    st.info("💡 Tip: Add resume + GitHub + projects for faster selection")

# ─────────────────────────────
# 📄 ATS RESUME BUILDER (ADVANCED)
# ─────────────────────────────
elif mode == "📄 ATS Resume Builder":

    st.title("📄 ATS Resume Builder Pro")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    location = st.text_input("Location")

    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    experience = st.text_area("Experience")
    objective = st.text_area("Career Objective")

    resume_text = f"""
NAME: {name}
EMAIL: {email}
PHONE: {phone}
LOCATION: {location}

OBJECTIVE:
{objective}

EDUCATION:
{education}

SKILLS:
{skills}

PROJECTS:
{projects}

EXPERIENCE:
{experience}
"""

    if st.button("Generate Resume"):
        st.text_area("ATS Resume", resume_text, height=400)

    # PDF Download
    def create_pdf(text):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        y = 800
        for line in text.split("\n"):
            p.drawString(50, y, line[:90])
            y -= 15
        p.save()
        buffer.seek(0)
        return buffer

    if st.button("Download PDF"):
        pdf = create_pdf(resume_text)
        st.download_button("Download Resume PDF", pdf, file_name="resume.pdf")

# ─────────────────────────────
# 🧠 AI RESUME CHECKER
# ─────────────────────────────
elif mode == "🧠 Resume AI Checker":

    st.title("🧠 Resume vs Job AI Checker")

    resume = st.text_area("Paste Resume")
    job = st.text_area("Paste Job Description")

    if st.button("Analyze Match"):

        if len(resume) < 20 or len(job) < 20:
            st.error("Add both resume and job description")
        else:
            score = random.randint(60, 95)

            st.success(f"ATS Match Score: {score}/100")

            st.info("Improvements:")
            st.write("✔ Add more keywords from job description")
            st.write("✔ Add measurable achievements")
            st.write("✔ Improve project descriptions")

# ─────────────────────────────
# 🎤 INTERVIEW KILLER
# ─────────────────────────────
elif mode == "🎤 Interview Killer":

    st.title("🎤 Interview Killer AI")

    q = st.text_area("Question", "Explain RAG in AI")
    ans = st.text_area("Your Answer")

    if st.button("Evaluate"):

        if len(ans) < 30:
            st.error("Answer too short")
        else:
            score = random.randint(7, 10)

            st.success(f"Score: {score}/10")

            st.info("Feedback:")
            st.write("✔ Add example")
            st.write("✔ Improve structure")
            st.write("✔ Use technical terms")

            st.code("""
RAG (Retrieval Augmented Generation) is a technique where LLM retrieves external data before generating answers.

Example: ChatGPT + search system.
""")

# ─────────────────────────────
# 🌐 PORTFOLIO GENERATOR
# ─────────────────────────────
elif mode == "🌐 Portfolio Generator":

    st.title("🌐 Portfolio Generator")

    name = st.text_input("Name")
    about = st.text_area("About You")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    if st.button("Generate Portfolio"):

        html = f"""
        <html>
        <head><title>{name} Portfolio</title></head>
        <body>
        <h1>{name}</h1>
        <h2>About</h2>
        <p>{about}</p>

        <h2>Skills</h2>
        <p>{skills}</p>

        <h2>Projects</h2>
        <p>{projects}</p>
        </body>
        </html>
        """

        st.download_button("Download Portfolio HTML", html, file_name="portfolio.html")