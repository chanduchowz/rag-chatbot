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
import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

load_dotenv()

st.set_page_config(page_title="AI Tutor 🤖", page_icon="🧠", layout="wide")

# Sidebar
with st.sidebar:
    st.image("https://em-content.zobj.net/source/twitter/376/robot_1f916.png", width=80)
    st.title("🧠 AI Tutor")
    st.markdown("---")
    mode = st.radio("Choose Mode:", ["💬 Chat & Learn", "🎯 Quiz Me!", "💡 Daily AI Fact"])
    st.markdown("---")
    st.markdown("**Topics I cover:**")
    st.markdown("✅ Artificial Intelligence")
    st.markdown("✅ Machine Learning")
    st.markdown("✅ Deep Learning")
    st.markdown("✅ Gen AI & LLMs")
    st.markdown("✅ Python & Tools")
    st.markdown("✅ Career Advice")
    st.markdown("✅ Any topic!")
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.markdown("💪 **Keep learning, keep growing!**")
    st.markdown("🔥 You're doing amazing!")

# Daily facts
facts = [
    "🤖 The term 'Artificial Intelligence' was coined by John McCarthy in 1956!",
    "🧠 GPT-4 has around 1.76 trillion parameters!",
    "📊 Machine Learning is used by Netflix to save $1 billion/year in customer retention!",
    "🚗 Tesla's Autopilot uses Deep Learning to process 1.4 billion miles of real-world driving data!",
    "💡 The first chatbot, ELIZA, was created in 1966 at MIT!",
    "🎮 AlphaGo beat the world champion Go player in 2016 using Deep Reinforcement Learning!",
    "📱 Your phone's face recognition uses a Convolutional Neural Network (CNN)!",
    "🌍 India is the 3rd largest AI talent pool in the world!",
    "💼 AI Engineer is the #1 fastest growing job in Hyderabad in 2026!",
    "🔥 LangChain was created in 2022 and already has 500K+ GitHub stars!",
]

quizzes = [
    {
        "q": "What does 'ML' stand for?",
        "options": ["Machine Logic", "Machine Learning", "Model Learning", "Meta Learning"],
        "answer": "Machine Learning",
        "explanation": "ML stands for Machine Learning — teaching machines to learn from data!"
    },
    {
        "q": "Which algorithm is used for classification problems?",
        "options": ["Linear Regression", "K-Means", "Random Forest", "PCA"],
        "answer": "Random Forest",
        "explanation": "Random Forest is an ensemble method great for classification!"
    },
    {
        "q": "What is a Neural Network inspired by?",
        "options": ["Computer circuits", "Human brain", "Decision trees", "Statistics"],
        "answer": "Human brain",
        "explanation": "Neural Networks are inspired by neurons in the human brain!"
    },
    {
        "q": "What does RAG stand for in Gen AI?",
        "options": ["Random Activation Graph", "Retrieval Augmented Generation", "Recurrent AI Graph", "Real AI Generation"],
        "answer": "Retrieval Augmented Generation",
        "explanation": "RAG = Retrieval Augmented Generation — combining search with LLMs!"
    },
    {
        "q": "Which company created ChatGPT?",
        "options": ["Google", "Meta", "OpenAI", "Microsoft"],
        "answer": "OpenAI",
        "explanation": "ChatGPT was created by OpenAI, founded by Sam Altman!"
    },
    {
        "q": "What is overfitting in ML?",
        "options": ["Model too simple", "Model memorizes training data", "Model trains too fast", "Model uses too little data"],
        "answer": "Model memorizes training data",
        "explanation": "Overfitting = model memorizes training data and fails on new data!"
    },
    {
        "q": "What is a Transformer in AI?",
        "options": ["A robot", "A power device", "An attention-based neural network", "A data cleaner"],
        "answer": "An attention-based neural network",
        "explanation": "Transformers use attention mechanisms — the backbone of all LLMs like GPT!"
    },
    {
        "q": "What does LLM stand for?",
        "options": ["Large Logic Model", "Long Language Model", "Large Language Model", "Linear Learning Model"],
        "answer": "Large Language Model",
        "explanation": "LLM = Large Language Model — AI trained on massive text data!"
    },
]

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
You are an enthusiastic, world-class AI/ML/Deep Learning/Gen AI tutor and mentor!
Your goal is to make learning fun, easy and exciting for everyone.

Rules:
- Use the context below if relevant, otherwise use your vast knowledge
- Always explain with real-world examples (Netflix, Google, Tesla, Instagram etc.)
- Use emojis to make answers engaging 🎯
- Break complex topics into simple steps
- Add fun facts where relevant
- Be encouraging and positive — celebrate the user's curiosity!
- For coding questions, provide working code with explanations
- For career questions, give practical Hyderabad job market advice
- End answers with a motivational tip or a follow-up question to keep them engaged

Context: {context}
Question: {question}
Answer:
""")
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

chain = load_chain()

# ─── CHAT MODE ───
if mode == "💬 Chat & Learn":
    st.title("💬 Chat & Learn")
    st.caption("Ask me anything — AI, ML, DL, Gen AI, Python, career advice and more!")

    motivational = [
        "🔥 Every expert was once a beginner. Keep going!",
        "💡 Curiosity is the engine of learning!",
        "🚀 You're one question away from your next breakthrough!",
        "🧠 Your brain grows every time you learn something new!",
    ]
    st.info(random.choice(motivational))

    if "messages" not in st.session_state:
        st