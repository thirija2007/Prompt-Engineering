import streamlit as st
from llm import ask_llm
from prompt_templates import build_prompt

st.set_page_config(
    page_title="PromptLab",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PromptLab")
st.subheader("LLM Prompt Template Explorer")

st.write(
    "Explore prompting techniques and generate answers "
    "to your questions using a Large Language Model."
)

# Prompt Settings
st.sidebar.header("Prompt Settings")

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
    value=500,
    step=100
)

# User Input
st.markdown("### Enter Your Task")

task = st.text_area(
    "Your Question",
    placeholder="Example: What is Python?",
    height=120
)

if st.button("🚀 Generate Answer"):

    if not task.strip():
        st.warning("Please enter your question.")

    else:
        prompt = build_prompt(technique, task)

        st.markdown("### 🔍 Generated Prompt")
        st.code(prompt, language="text")

        try:
            with st.spinner("Generating answer..."):
                answer = ask_llm(
                    prompt,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            st.markdown("### 💡 LLM Response")
            st.write(answer)

        except Exception as error:
            st.error(
                "The LLM could not generate a response. "
                "Please check your Hugging Face token and model."
            )
            st.caption(str(error))

st.divider()
st.caption("PromptLab | Prompt Engineering | Streamlit + Qwen")
