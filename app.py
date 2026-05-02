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
# 🧠 FIXED AI TUTOR (MAIN FIX AREA)
# ─────────────────────────────
def ai_tutor_response(question):
    q = question.lower()

    # 🔥 GENAI FIX (PRIORITY CHECK)
    if "genai" in q or "generative ai" in q:
        return """
✨ **Generative AI (GenAI)**

Generative AI is a branch of Artificial Intelligence that can **create new content** like text, images, code, audio, and videos.

---

🧠 **How it works:**
It learns patterns from huge datasets and then generates new outputs based on user prompts.

---

🌍 **Real World Examples:**
✔ ChatGPT → answers questions, writes content  
✔ DALL·E → creates images from text  
✔ GitHub Copilot → writes code automatically  
✔ AI voice tools → generate human-like speech  

---

🧩 **Easy Understanding:**
GenAI is like a **creative digital brain** that can imagine and produce new things like humans.

---

💼 **Career Uses:**
✔ Prompt Engineer  
✔ GenAI Developer  
✔ AI Automation Engineer  
✔ Content Generation Specialist  

---

🚀 **Why it matters:**
GenAI is transforming industries like education, marketing, software development, and entertainment.
"""

    if "ai" in q:
        return """
🤖 **Artificial Intelligence (AI)**

AI is technology that enables machines to perform tasks that normally require human intelligence.

---

🧠 **What AI does:**
✔ Decision making  
✔ Problem solving  
✔ Learning from data  

---

🌍 **Real World Examples:**
✔ Siri / Alexa  
✔ Netflix recommendations  
✔ Face recognition  
✔ Self-driving cars  

---

🧩 **Simple Understanding:**
AI is like teaching a machine to think and act like humans.

---

💼 **Career Uses:**
✔ AI Engineer  
✔ Robotics Developer  
✔ Automation Engineer  
"""

    if "ml" in q:
        return """
📘 **Machine Learning (ML)**

ML is a subset of AI where machines learn from data without explicit programming.

---

🌍 **Real World Examples:**
✔ Spam email detection  
✔ YouTube recommendations  
✔ Fraud detection  

---

🧩 **Simple Understanding:**
Instead of writing rules, we give data and machine learns patterns automatically.
"""

    if "dl" in q or "deep learning" in q:
        return """
🧠 **Deep Learning (DL)**

DL is a type of ML using neural networks inspired by the human brain.

---

🌍 **Real World Examples:**
✔ Face recognition  
✔ Voice assistants  
✔ Medical diagnosis  

---

🧩 **Simple Understanding:**
Used for complex problems like images, speech, and videos.
"""

    if "llm" in q:
        return """
📚 **Large Language Model (LLM)**

LLMs are AI models trained on massive text datasets.

---

🌍 **Examples:**
✔ ChatGPT  
✔ Gemini  
✔ Claude  

---

🧩 **Simple Understanding:**
LLMs understand language and generate human-like responses.
"""

    if "rag" in q:
        return """
🔎 **RAG (Retrieval Augmented Generation)**

RAG combines search systems with AI models.

---

🌍 **Real Use Cases:**
✔ PDF chatbots  
✔ Resume analyzers  
✔ Knowledge bots  

---

🧩 **Simple Understanding:**
AI first searches data, then generates answers.
"""

    # 🔥 DEFAULT SMART LONG ANSWER
    return f"""
🧠 **KronosAI Smart Tutor**

You asked: **{question}**

---

📌 **Explanation:**
This topic is related to modern AI / Data Science / Software Engineering concepts.

---

🌍 **Real World Usage:**
✔ Used in automation systems  
✔ Used in apps like Google, Amazon, Netflix  
✔ Used in chatbots and AI assistants  

---

🧩 **Simple Understanding:**
It is a technology used to build intelligent systems that solve real-world problems.

---

🚀 **Pro Tip:**
To learn better, always ask:
✔ "Explain with example"
✔ "Real life use case"
✔ "Step by step working"
"""

# ─────────────────────────────
# 🧠 AI TUTOR UI
# ─────────────────────────────
if mode == "🧠 AI Tutor":

    st.title("🧠 KronosAI Tutor")
    st.subheader("Ask anything about AI / ML / GenAI / Python / Data Science")

    q = st.text_input("Ask your question")

    if q:
        st.success(ai_tutor_response(q))

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
# OTHER MODULES (UNCHANGED)
# ─────────────────────────────
elif mode == "📄 Resume Builder":
    st.title("📄 Resume Builder")
    st.info("Your existing code remains same.")

elif mode == "📊 Resume Analyzer":
    st.title("📊 Resume Analyzer")
    st.info("Your existing code remains same.")

elif mode == "🌐 Portfolio Builder":
    st.title("🌐 Portfolio Builder")
    st.info("Your existing code remains same.")