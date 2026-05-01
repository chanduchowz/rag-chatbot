import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
import random

os.environ["TRANSFORMERS_VERBOSITY"] = "error"
load_dotenv()

st.set_page_config(page_title="KronosAI Pro 🚀", page_icon="🧠", layout="wide")

# ─────────────────────────────
# SIDEBAR
# ─────────────────────────────
with st.sidebar:
    st.title("⚡ KronosAI PRO")
    st.markdown("AI Tutor + Job Engine + Interview Trainer 🚀")

    mode = st.radio(
        "Select Mode",
        ["💬 AI Tutor", "💼 Job Board", "🎤 Mock Interview", "📄 Resume Builder"]
    )

    if st.button("Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# ─────────────────────────────
# STRICT AI PROMPT (NO CONFUSION)
# ─────────────────────────────
def prompt_engine():
    return ChatPromptTemplate.from_template("""
You are KronosAI Pro 🤖.

RULES:
- Be precise and factual
- Do NOT mix concepts (RAG ≠ AI general explanation)
- If unknown, say "Not enough data"
- Use context only when relevant

Context:
{context}

Question:
{question}

Answer:
""")

# ─────────────────────────────
# MODEL
# ─────────────────────────────
@st.cache_resource
def load_chain():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=st.secrets["GROQ_API_KEY"]
    )

    def format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

    return (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt_engine()
        | llm
        | StrOutputParser()
    )

chain = load_chain()

# ─────────────────────────────
# AI TUTOR
# ─────────────────────────────
if mode == "💬 AI Tutor":

    st.title("🧠 KronosAI Tutor")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    q = st.chat_input("Ask AI / RAG / GenAI / ML / Career...")

    if q:
        st.session_state.messages.append({"role": "user", "content": q})

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                ans = chain.invoke(q)
                st.markdown(ans)

        st.session_state.messages.append({"role": "assistant", "content": ans})

# ─────────────────────────────
# JOB BOARD (FRESHERS + EXP)
# ─────────────────────────────
elif mode == "💼 Job Board":

    st.title("💼 AI Job Engine")

    level = st.selectbox("Select Experience Level", ["Fresher", "1-3 Years", "3+ Years"])

    jobs = {
        "Fresher": [
            "Data Analyst Intern - Python, SQL",
            "AI/ML Intern - Basic ML knowledge",
            "Business Analyst Trainee",
            "Python Developer Fresher"
        ],
        "1-3 Years": [
            "Data Analyst - Power BI, SQL",
            "ML Engineer - Scikit-learn, NLP",
            "Backend Developer - Python FastAPI"
        ],
        "3+ Years": [
            "Senior Data Scientist",
            "AI Engineer - LLM / RAG systems",
            "Data Engineering Lead - Azure / AWS"
        ]
    }

    st.subheader("🔥 Recommended Jobs")

    for j in jobs[level]:
        st.success(j)

    st.info("💡 Tip: Apply daily 10–15 jobs + build 2 strong projects")

# ─────────────────────────────
# MOCK INTERVIEW
# ─────────────────────────────
elif mode == "🎤 Mock Interview":

    st.title("🎤 AI Interview Trainer")

    questions = [
        "Explain RAG in AI",
        "What is overfitting?",
        "Explain difference between AI and ML",
        "What is a vector database?",
        "Explain your final project"
    ]

    q = random.choice(questions)

    st.subheader("Question:")
    st.warning(q)

    ans = st.text_area("Your Answer:")

    if st.button("Evaluate"):

        if len(ans) < 20:
            st.error("❌ Answer too short")
        else:
            st.success("✅ Good structure")
            st.info("💡 Improve: Add examples + technical depth + clarity")

# ─────────────────────────────
# RESUME BUILDER
# ─────────────────────────────
elif mode == "📄 Resume Builder":

    st.title("📄 Resume Generator")

    name = st.text_input("Your Name")
    skills = st.text_area("Skills (comma separated)")
    projects = st.text_area("Projects")

    if st.button("Generate Resume"):

        resume = f"""
NAME: {name}

SKILLS:
{skills}

PROJECTS:
{projects}

OBJECTIVE:
Seeking a role in Data Science / AI / Analytics to apply skills in real-world problems.
"""

        st.text_area("Your Resume", resume, height=300)     