def build_prompt(technique, task):
    base = f"""
You are a helpful, knowledgeable AI assistant.

Answer the user's actual request, whatever the topic.
Understand the question before answering.
Use simple language and provide accurate, relevant information.
If the user requests code, provide complete code in the
requested programming language with a brief explanation.
If the user asks for a definition, explain it clearly.
If the user asks for steps, provide them in order.
Do not assume every question is about Python or React.

User's request:
{task}
"""

    if technique == "Zero-shot":
        return base

    elif technique == "One-shot":
        return f"""
{base}

Example format:
Question: What is a database?
Answer: A database is an organized collection of data.
Follow this example's clear and simple style.
"""

    elif technique == "Few-shot":
        return f"""
{base}

Follow these examples of answering different requests:
- Definition questions: give a clear definition and example.
- Programming questions: provide code and explain it.
- How-to questions: give numbered steps.
Choose the format that best matches the user's request.
"""

    elif technique == "CoT":
        return f"""
{base}

Work through the problem carefully. Provide the final answer
and a concise explanation of the key steps, without revealing
hidden internal reasoning.
"""

    elif technique == "Manual CoT":
        return f"""
{base}

Use these steps when appropriate:
1. Understand the request.
2. Identify the important requirements.
3. Prepare the answer.
4. Present the result clearly.
"""

    elif technique == "ToT":
        return f"""
{base}

Consider different approaches when the task benefits from it.
Choose the most suitable approach and present the final answer.
Avoid unnecessary alternatives.
"""

    return base
