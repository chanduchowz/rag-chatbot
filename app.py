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

# ─────────────────────────────
# ENV SETUP
# ─────────────────────────────
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
load_dotenv()

st.set_page_config(page_title="AI Tutor 🤖", page_icon="🧠", layout="wide")

# ─────────────────────────────
# SIDEBAR
# ─────────────────────────────
with st.sidebar:
    st.image("https://em-content.zobj.net/source/twitter/376/robot_1f916.png", width=80)
    st.title("🧠 AI Tutor")

    st.markdown("---")
    mode = st.radio("Choose Mode:", ["💬 Chat & Learn", "🎯 Quiz Me!", "💡 Daily AI Fact"])

    st.markdown("---")
    st.markdown("**Topics I cover:**")
    st.markdown("✅ AI / ML / DL")
    st.markdown("✅ Gen AI & LLMs")
    st.markdown("✅ Python & Tools")
    st.markdown("✅ Career Advice")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("🔥 Keep learning, keep growing!")

# ─────────────────────────────
# DATA
# ─────────────────────────────
facts = [
    "🤖 AI started in 1956 at Dartmouth Conference!",
    "🧠 GPT models predict next words using deep learning.",
    "📊 Netflix uses ML for recommendations.",
    "🚗 Tesla uses AI for self-driving.",
    "💡 ELIZA was first chatbot in 1966.",
]

quizzes = [
    {
        "q": "What does ML stand for?",
        "options": ["Machine Logic", "Machine Learning", "Meta Learning", "Model Learning"],
        "answer": "Machine Learning",
        "explanation": "ML = Machine Learning 🎯"
    },
    {
        "q": "What does LLM stand for?",
        "options": ["Large Language Model", "Long Logic Machine", "Linear Learning Model", "Language Logic Machine"],
        "answer": "Large Language Model",
        "explanation": "LLM = Large Language Model 🚀"
    }
]

# ─────────────────────────────
# LLM + RAG CHAIN
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

    # ✅ STREAMLIT CLOUD SAFE SECRET HANDLING
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=st.secrets["GROQ_API_KEY"]
    )

    prompt = ChatPromptTemplate.from_template("""
You are an expert AI tutor 🤖

Rules:
- Explain simply
- Use real-world examples
- Use emojis
- Be motivating and friendly

Context:
{context}

Question:
{question}

Answer:
""")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

chain = load_chain()

# ─────────────────────────────
# CHAT MODE
# ─────────────────────────────
if mode == "💬 Chat & Learn":

    st.title("💬 Chat & Learn")
    st.caption("Ask anything about AI, ML, Python, GenAI 🚀")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type your question...")

    if user_input:

        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking... 🤔"):
                response = chain.invoke(user_input)
                st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

# ─────────────────────────────
# QUIZ MODE
# ─────────────────────────────
elif mode == "🎯 Quiz Me!":

    st.title("🎯 Quiz Time!")

    q = random.choice(quizzes)

    st.subheader(q["q"])
    answer = st.radio("Choose answer:", q["options"])

    if st.button("Submit"):
        if answer == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Wrong!")

        st.info(q["explanation"])

# ─────────────────────────────
# FACT MODE
# ─────────────────────────────
elif mode == "💡 Daily AI Fact":

    st.title("💡 AI Fact")

    st.success(random.choice(facts))