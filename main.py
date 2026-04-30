import streamlit as st
import os
import random

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# ---------------- ENV SETUP ----------------
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

if os.path.exists(".env"):
    load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Tutor 🤖", page_icon="🧠", layout="wide")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.image("https://em-content.zobj.net/source/twitter/376/robot_1f916.png", width=80)
    st.title("🧠 AI Tutor")
    st.markdown("---")

    mode = st.radio(
        "Choose Mode:",
        ["💬 Chat & Learn", "🎯 Quiz Me!", "💡 Daily AI Fact"]
    )

    st.markdown("---")
    st.markdown("**Topics I cover:**")
    st.markdown("""
    ✅ Artificial Intelligence  
    ✅ Machine Learning  
    ✅ Deep Learning  
    ✅ Gen AI & LLMs  
    ✅ Python & Tools  
    ✅ Career Advice  
    """)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- FACTS ----------------
facts = [
    "🤖 AI was coined in 1956 by John McCarthy",
    "🧠 GPT models are trained on billions of words",
    "🚗 Tesla uses deep learning for autopilot",
    "📱 Face unlock uses neural networks",
]

# ---------------- QUIZ ----------------
quizzes = [
    {
        "q": "What does ML stand for?",
        "options": ["Machine Logic", "Machine Learning", "Model Learning", "Meta Learning"],
        "answer": "Machine Learning",
    },
    {
        "q": "What is LLM?",
        "options": ["Large Language Model", "Long Logic Model", "Learning Language Machine", "None"],
        "answer": "Large Language Model",
    },
]

# ---------------- LLM CHAIN ----------------
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
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template("""
You are an expert AI tutor.

Use context if available, otherwise answer from knowledge.

Make answers:
- simple
- beginner friendly
- with examples
- with emojis

Context: {context}
Question: {question}
Answer:
""")

    def format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

chain = load_chain()

# ---------------- INIT SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CHAT MODE ----------------
if mode == "💬 Chat & Learn":

    st.title("💬 Chat & Learn AI Tutor")

    user_input = st.chat_input("Ask anything about AI, ML, Gen AI...")

    if user_input:
        st.session_state.messages.append(("user", user_input))

        response = chain.invoke(user_input)

        st.session_state.messages.append(("ai", response))

    for role, msg in st.session_state.messages:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

# ---------------- QUIZ MODE ----------------
elif mode == "🎯 Quiz Me!":

    st.title("🎯 AI Quiz")

    q = random.choice(quizzes)

    st.subheader(q["q"])

    answer = st.radio("Choose answer:", q["options"])

    if st.button("Submit"):
        if answer == q["answer"]:
            st.success("Correct 🎉")
        else:
            st.error("Wrong ❌")
            st.info(f"Correct answer: {q['answer']}")

# ---------------- FACT MODE ----------------
elif mode == "💡 Daily AI Fact":

    st.title("💡 Daily AI Fact")
    st.info(random.choice(facts))