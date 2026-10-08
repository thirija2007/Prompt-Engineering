def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Answer this React task directly and accurately.

Task:
{task}

Provide:
1. A short explanation
2. Complete React code
3. Brief explanation of the code
""".strip()


    elif technique == "One-shot":
        return f"""
Use the example below to understand the expected style.

Example:
Task: Create a React greeting component.
Answer: Create a functional React component using JSX
to display "Hello, Student!".

Now answer this task:
{task}

Provide:
1. A short explanation
2. Complete React code
3. Brief explanation of the code
""".strip()


    elif technique == "Few-shot":
        return f"""
Study the examples and follow their style.

Example 1:
Task: Display a username.
Answer: Use JSX to display the username.

Example 2:
Task: Create a counter.
Answer: Use React useState to store and update the counter.

Example 3:
Task: Handle a button click.
Answer: Use an onClick event handler.

Now answer this task:
{task}

Provide complete React code and a short explanation.
""".strip()


    elif technique == "CoT":
        return f"""
Solve the following React task carefully.

First identify the requirements.
Then identify the required React components and features.
Finally provide the solution.

Do not reveal private/internal chain-of-thought.
Provide only a short explanation of the key steps.

Task:
{task}
""".strip()


    elif technique == "Manual CoT":
        return f"""
Use the following explicit structure.

Step 1: Understand the task.

Step 2: Identify the React components.

Step 3: Identify required state, props, events, or hooks.

Step 4: Write the complete React code.

Step 5: Verify the solution.

Task:
{task}
""".strip()


    elif technique == "ToT":
        return f"""
Solve the React task using multiple approaches.

Approach A:
Suggest one possible React solution.

Approach B:
Suggest another React solution.

Approach C:
Suggest another solution when useful.

Selection:
Compare the approaches and select the most suitable one.

Final answer:
Provide the selected solution with complete React code
and a concise explanation.

Do not reveal private/internal chain-of-thought.

Task:
{task}
""".strip()


    else:
        raise ValueError("Unknown prompting technique")