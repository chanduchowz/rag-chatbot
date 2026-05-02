# ─────────────────────────────
# 🧠 AI TUTOR — Powered by Claude API
# ─────────────────────────────
if mode == "🧠 AI Tutor":
    import anthropic

    st.title("🧠 KronosAI Tutor")
    st.subheader("Ask anything about AI · ML · GenAI · Python · LLMs · Tools · Careers")

    # ── Suggestion chips ──
    suggestions = [
        "How does Generative AI work?",
        "What is RAG and how is it used?",
        "Explain LangChain with examples",
        "Fine-tuning vs RAG — which to use?",
        "Best Python libraries for AI in 2025",
        "What is an AI Agent? How to build one?",
        "Explain Embeddings & Vector Databases",
        "How does Prompt Engineering work?",
    ]

    st.markdown("**💡 Try asking:**")
    cols = st.columns(4)
    for i, s in enumerate(suggestions):
        if cols[i % 4].button(s, key=f"sug_{i}", use_container_width=True):
            st.session_state["tutor_question"] = s

    st.divider()

    # ── Question input ──
    if "tutor_question" not in st.session_state:
        st.session_state["tutor_question"] = ""

    q = st.text_input(
        "Ask your question",
        value=st.session_state["tutor_question"],
        placeholder="e.g. How does attention mechanism work in transformers?",
        key="tutor_input"
    )

    SYSTEM_PROMPT = """You are KronosAI Tutor — an expert instructor for AI, ML, Deep Learning, GenAI, Python, Data Science, and all modern AI tools.

RULES:
1. Answer ANY question about: AI, ML, DL, GenAI, LLMs, RAG, Python, LangChain, n8n, Ollama, Hugging Face, vector databases, embeddings, prompt engineering, AI agents, fine-tuning, NLP, computer vision, MLOps, cloud AI, AI careers, and related tools.
2. ALWAYS give a COMPLETE, DETAILED answer — never refuse or say "ask about AI/ML" for tech topics.
3. Structure every answer with these sections:

   🔍 SIMPLE EXPLANATION — What it is in plain language (2-3 sentences)
   
   ⚙️ HOW IT WORKS — Technical explanation (step-by-step if needed)
   
   🌍 REAL-WORLD EXAMPLES — 3 to 5 named, concrete examples (e.g. Netflix uses X for Y, Uber uses X for Z)
   
   🐍 CODE SNIPPET — Python code example when relevant (practical, runnable)
   
   💼 CAREER RELEVANCE — Which job roles use this skill and at which companies
   
   ✅ KEY TAKEAWAY — 1-2 sentence summary

4. If the user asks a 1-line question, still give a full structured answer.
5. Use markdown formatting: **bold**, ### headers, bullet points, code blocks.
6. After your full answer, add 3 follow-up question suggestions like this:
   ---
   **💡 Explore further:**
   - [question 1]
   - [question 2]  
   - [question 3]
"""

    if q:
        st.session_state["tutor_question"] = ""
        with st.spinner("🧠 KronosAI is thinking..."):
            try:
                client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var
                message = client.messages.create(
                    model="claude-opus-4-5",
                    max_tokens=2048,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": q}]
                )
                answer = message.content[0].text
                st.markdown("---")
                st.markdown(answer)
            except Exception as e:
                st.error(f"❌ Could not connect to AI: {e}")
                st.info("Make sure your ANTHROPIC_API_KEY environment variable is set.")