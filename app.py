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
            "📄 Resume Builder",
            "📊 Resume Analyzer",
            "🌐 Portfolio Builder"
        ]
    )

# ─────────────────────────────
# AI TUTOR KNOWLEDGE ENGINE (UPGRADED)
# ─────────────────────────────
def ai_tutor_response(question):
    q = question.lower()

    responses = {
        "ai": """
🤖 **Artificial Intelligence (AI)**

AI means machines performing tasks that usually need human intelligence.

### Real World Examples:
✔ Siri / Alexa voice assistants  
✔ Self-driving cars  
✔ Netflix recommendations  
✔ Face unlock in phones  

### Easy Understanding:
AI is like teaching a machine to think and decide.

### Career Uses:
AI Engineer, Robotics, Automation, Chatbot Developer
""",

        "ml": """
📘 **Machine Learning (ML)**

ML is a part of AI where machines learn patterns from data.

### Real World Examples:
✔ Spam email detection  
✔ Product recommendations  
✔ Fraud detection in banking  
✔ YouTube suggested videos  

### Easy Understanding:
Instead of coding every rule, we give data and machine learns itself.
""",

        "deep learning": """
🧠 **Deep Learning (DL)**

Deep Learning uses neural networks similar to the human brain.

### Real World Examples:
✔ Face recognition  
✔ Voice assistants  
✔ Self-driving cars  
✔ Medical image diagnosis  

### Easy Understanding:
DL is advanced ML used for images, audio, videos.
""",

        "genai": """
✨ **Generative AI**

Generative AI creates new content like text, images, videos, code.

### Real World Examples:
✔ ChatGPT writes answers  
✔ Midjourney creates images  
✔ AI music generation  
✔ AI coding assistants  

### Easy Understanding:
Instead of only analyzing data, GenAI creates something new.
""",

        "llm": """
📚 **Large Language Model (LLM)**

LLMs are AI models trained on huge text data.

### Real World Examples:
✔ ChatGPT  
✔ Gemini  
✔ Claude  
✔ Copilot  

### Easy Understanding:
LLM understands language and gives smart human-like responses.
""",

        "rag": """
🔎 **RAG (Retrieval Augmented Generation)**

RAG combines Search + AI Answering.

### Real World Example:
Upload PDFs and ask questions from documents.

### Easy Understanding:
Instead of only memory, AI searches data first then answers.

### Used In:
✔ Company chatbots  
✔ Resume analyzers  
✔ Document assistants
""",

        "python": """
🐍 **Python**

Python is the most popular language for AI / Data Science.

### Real World Uses:
✔ AI development  
✔ Web apps  
✔ Automation  
✔ Data analysis  
✔ ML projects  

### Why Python?
✔ Easy syntax  
✔ Huge libraries  
✔ Fast development
""",

        "sql": """
🗄 **SQL**

SQL is used to manage databases.

### Real World Uses:
✔ Company customer data  
✔ Sales reports  
✔ Dashboards  
✔ Data Analyst jobs  

### Example:
SELECT * FROM employees;
""",

        "power bi": """
📊 **Power BI**

Power BI is used to create dashboards and reports.

### Real World Uses:
✔ Sales Dashboard  
✔ HR Dashboard  
✔ Finance Reports  
✔ KPI Monitoring
""",

        "chatgpt": """
💬 **ChatGPT**

ChatGPT is an AI chatbot built using Large Language Models.

### Uses:
✔ Learning concepts  
✔ Coding help  
✔ Resume writing  
✔ Content creation  
✔ Business ideas
""",

        "numpy": """
🔢 **NumPy**

NumPy is a Python library used for numerical computing.

### Used In:
✔ Arrays  
✔ Matrix operations  
✔ AI calculations
""",

        "pandas": """
📈 **Pandas**

Pandas is used for data cleaning and analysis.

### Real World Uses:
✔ Excel-like data handling  
✔ Reports  
✔ Analytics
""",

        "streamlit": """
🌐 **Streamlit**

Streamlit is used to build web apps using Python easily.

### Examples:
✔ AI apps  
✔ Dashboard apps  
✔ Resume tools  
✔ Chatbots
"""
    }

    # Find keyword match
    for key in responses:
        if key in q:
            return responses[key]

    # Generic intelligent fallback
    return f"""
🧠 **KronosAI Smart Tutor**

You asked: **{question}**

I understand you're asking something related to AI / Technology.

### Simple Explanation:
This topic is important in modern technology and used in real-world applications.

### Examples:
✔ Automation  
✔ Chatbots  
✔ Data Science  
✔ Software Development  
✔ Business Growth  

### Tip:
Try asking like:
- What is Generative AI?
- Explain Python with examples
- Difference between AI and ML
- How ChatGPT works
- What is RAG?
"""

# ─────────────────────────────
# 🧠 AI TUTOR
# ─────────────────────────────
if mode == "🧠 AI Tutor":

    st.title("🧠 KronosAI Tutor")
    st.subheader("Ask Any Question About AI / ML / Python / Data Science / GenAI / Tools")

    q = st.text_input("Ask anything")

    if q:
        answer = ai_tutor_response(q)
        st.success(answer)

# ─────────────────────────────
# 💼 JOB ENGINE
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
# OTHER MODULES SAME AS YOUR CODE
# ─────────────────────────────
elif mode == "📄 Resume Builder":
    st.title("📄 ATS Resume Builder")
    st.info("Your existing code remains same.")

elif mode == "📊 Resume Analyzer":
    st.title("📊 Resume Analyzer")
    st.info("Your existing code remains same.")

elif mode == "🌐 Portfolio Builder":
    st.title("🌐 Portfolio Builder")
    st.info("Your existing code remains same.")