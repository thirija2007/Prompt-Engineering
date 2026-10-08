#  PromptLab – LLM Prompt Template Explorer

##  Project Overview

PromptLab is a Streamlit-based prompt engineering application designed to demonstrate different prompting techniques for technical React development tasks.

The application allows users to select a prompting technique, enter a React task, and view the generated prompt along with a sample React solution.

##  Objectives

* Understand different LLM prompting techniques
* Generate structured prompts for React development tasks
* Compare Zero-shot, One-shot, Few-shot, CoT, Manual CoT, and ToT prompting
* Provide a simple and interactive Streamlit interface
* Demonstrate prompt engineering concepts using a practical technical example

## Live Demo

https://prompt-engineering-jtszaappptnpwke8acktyvs.streamlit.app/

##  Features

* Zero-shot prompting
* One-shot prompting
* Few-shot prompting
* Chain-of-Thought (CoT) prompting
* Manual CoT prompting
* Tree-of-Thought (ToT) prompting
* Temperature control
* React task input
* Generated prompt display
* React code output
* Simple Streamlit user interface

##  Technologies Used

* Python
* Streamlit
* Prompt Engineering
* React
* JSX

##  Project Structure

```text
Prompt Engineering/
│
├── app.py
├── prompt_templates.py
├── requirements.txt
├── README.md
└── .gitignore
```

##  Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Prompt-Engineering
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

##  How to Use

1. Open PromptLab.
2. Select a prompting technique from the sidebar.
3. Set the temperature value.
4. Enter a React development task.
5. Click **Generate Answer**.
6. View the generated prompt.
7. View the React solution and explanation.

##  Example

### Input

```text
Create a React component that displays three student names in a list.
```

### Generated Prompt

```text
Answer this React task directly.

Task:
Create a React component that displays three student names in a list.
```

### Generated Answer

The application produces a React functional component using an array of student names and the `map()` function to display them as a list.

##  Prompting Techniques

| Technique  | Description                            |
| ---------- | -------------------------------------- |
| Zero-shot  | Solves the task without examples       |
| One-shot   | Uses one example to guide the response |
| Few-shot   | Uses multiple examples                 |
| CoT        | Uses structured reasoning guidance     |
| Manual CoT | Provides explicit solution steps       |
| ToT        | Explores multiple possible approaches  |

##  Screenshots

Add your Streamlit screenshots here.

Example:
Zero-shot
<img width="1776" height="856" alt="Screenshot 2026-10-08 203544" src="https://github.com/user-attachments/assets/4bc77bea-06c7-4215-b89e-5ccda5ee8916" />
One-shot
<img width="1807" height="878" alt="Screenshot 2026-10-08 203618" src="https://github.com/user-attachments/assets/f5e2621a-1192-4bb8-a80c-95231773bf04" />
Few-shot
<img width="1857" height="867" alt="Screenshot 2026-10-08 203653" src="https://github.com/user-attachments/assets/5dc9ec88-a468-4497-a68e-f61e8744916f" />
CoT
<img width="1693" height="772" alt="Screenshot 2026-10-08 203739" src="https://github.com/user-attachments/assets/1d36815b-3178-4e9a-a74f-d61c6d94b159" />
Manual CoT
<img width="1755" height="771" alt="Screenshot 2026-10-08 203810" src="https://github.com/user-attachments/assets/cd3114ed-7353-481a-bdc8-9321f542a1de" />
ToT
<img width="1817" height="882" alt="Screenshot 2026-10-08 203835" src="https://github.com/user-attachments/assets/77d776d1-cd0f-4da6-ad6e-fe13f7130590" />

```

##  Author

**Thirija R**

B.Sc. Computer Science with Artificial Intelligence
