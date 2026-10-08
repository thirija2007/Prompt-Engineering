import streamlit as st


def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Answer this React task directly.

Task:
{task}
""".strip()

    elif technique == "One-shot":
        return f"""
Example:
Task: Create a React greeting component.
Answer: Create a functional React component using JSX.

Now answer this task:
{task}
""".strip()

    elif technique == "Few-shot":
        return f"""
Example 1:
Task: Display a username.
Answer: Use JSX to display the username.

Example 2:
Task: Create a counter.
Answer: Use React useState.

Now answer this task:
{task}
""".strip()

    elif technique == "CoT":
        return f"""
Understand the React task, identify the required components,
and provide the solution with a short explanation.

Task:
{task}
""".strip()

    elif technique == "Manual CoT":
        return f"""
Step 1: Understand the task.
Step 2: Identify the components.
Step 3: Identify required React features.
Step 4: Write the code.
Step 5: Verify the solution.

Task:
{task}
""".strip()

    elif technique == "ToT":
        return f"""
Approach A: Suggest one React solution.

Approach B: Suggest another React solution.

Selection: Choose the most suitable solution.

Task:
{task}
""".strip()


st.set_page_config(
    page_title="PromptLab",
    page_icon="🤖"
)

st.title("🤖 PromptLab")

st.subheader("LLM Prompt Template Explorer")

st.write(
    "A prompt engineering application for technical React tasks."
)

st.sidebar.header("Prompt Settings")

technique = st.sidebar.selectbox(
    "Choose Prompting Technique",
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
    0.0,
    1.0,
    0.3,
    0.1
)

st.markdown("### Enter Your React Task")

task = st.text_area(
    "React Task",
    placeholder="Create a React component that displays three student names in a list.",
    height=150
)

if st.button("🚀 Generate Answer"):

    if task.strip():

        prompt = build_prompt(
            technique,
            task
        )

        st.markdown("### 🔍 Generated Prompt")

        st.code(
            prompt,
            language="text"
        )

        st.markdown("### 💡 Generated Answer")

        react_code = '''import React from "react";

function StudentList() {
    const students = ["Arun", "Priya", "Rahul"];

    return (
        <div>
            <h2>Student List</h2>

            <ul>
                {students.map((student, index) => (
                    <li key={index}>{student}</li>
                ))}
            </ul>
        </div>
    );
}

export default StudentList;'''

        st.code(
            react_code,
            language="javascript"
        )

        st.write(
            "This React component stores three student names "
            "in an array and uses map() to display them as a list."
        )

    else:

        st.warning("Please enter a task.")

st.divider()

st.caption(
    "PromptLab | Prompt Engineering | Streamlit"
)