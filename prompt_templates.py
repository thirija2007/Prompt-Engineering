def build_prompt(technique, task):
    instruction = """
You are a helpful AI assistant.
Answer the user's actual question directly.
Do not assume the task is about React unless requested.
If code is requested, provide working code and a brief explanation.
"""

    if technique == "Zero-shot":
        return f"""
{instruction}

Task: {task}
"""

    elif technique == "One-shot":
        return f"""
{instruction}

Example:
Question: What is HTML?
Answer: HTML is the markup language used to structure web pages.

Now answer:
{task}
"""

    elif technique == "Few-shot":
        return f"""
{instruction}

Examples:
Question: What is Python?
Answer: Python is a programming language known for its simple syntax.

Question: What is SQL?
Answer: SQL is used to manage and query relational databases.

Now answer this question:
{task}
"""

    elif technique == "CoT":
        return f"""
{instruction}

Solve the task carefully. Provide a concise explanation
of the key steps without revealing hidden reasoning.

Task: {task}
"""

    elif technique == "Manual CoT":
        return f"""
{instruction}

Use this structure where appropriate:
1. Understand the question.
2. Identify the important points.
3. Formulate the answer.
4. Present the final answer clearly.

Task: {task}
"""

    elif technique == "ToT":
        return f"""
{instruction}

Consider different possible approaches when useful.
Choose the most suitable approach and give the final answer.
Do not include unnecessary alternatives.

Task: {task}
"""

    else:
        raise ValueError("Unknown prompting technique")
