import streamlit as st
from llm import ask_llm
from prompt_templates import build_prompt

st.set_page_config(
    page_title="PromptLab AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PromptLab AI")
st.subheader("LLM Prompt Engineering Playground")

st.write(
    "Explore prompting techniques and generate answers "
    "to questions on different topics."
)

st.info("Connected to Groq API. No Hugging Face token required.")

# Sidebar settings
st.sidebar.header("⚙️ Model Settings")

technique = st.sidebar.selectbox(
    "Select Prompting Technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.1
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=100,
    max_value=2000,
    value=600,
    step=100
)

# User task
st.header("📝 Enter Your Task")

task = st.text_area(
    "Type any question or task",
    placeholder=(
        "Examples:\n"
        "What is Python?\n"
        "Explain DBMS with an example.\n"
        "Write a Java program to add two numbers."
    ),
    height=150
)

if st.button("🚀 Generate Answer", type="primary"):
    if not task.strip():
        st.warning("Please enter a question or task.")
    else:
        try:
            with st.spinner("Generating answer using Groq..."):
                generated_prompt = build_prompt(
                    technique,
                    task.strip()
                )

                answer = ask_llm(
                    generated_prompt,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            st.success("Answer generated successfully!")

            st.subheader("🔍 Generated Prompt")
            st.code(generated_prompt, language="text")

            st.subheader("💡 LLM Response")
            st.markdown(answer)

        except Exception as e:
            st.error("The LLM could not generate a response.")
            st.code(str(e), language="text")

st.divider()
st.caption("PromptLab AI | Prompt Engineering Project")
