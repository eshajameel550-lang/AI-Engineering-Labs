# Task 3 - Self Correction AI Agent

## Objective

Build an AI agent that can generate Python code, evaluate it, detect errors, and automatically improve the code until it works correctly.

---

## Features

- Generates Python code using Gemini AI
- Evaluates syntax and runtime errors
- Detects logic errors
- Uses a self-correction loop
- Automatically retries until the code passes evaluation
- Uses temporary files for testing
- Supports Windows and VS Code

---

## Technologies Used

- Python
- Google Gemini API
- python-dotenv
- subprocess
- tempfile
- os

---

## Project Files

```
Task 3 Self Correction AI Agent
│
├── main.py
├── .env
├── README.md
├── output.txt
└── requirements.txt
```

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install google-generativeai python-dotenv
```

---

## Run the Project

```bash
python main.py
```

---

## Expected Output

- AI generates Python code.
- Evaluator checks the generated code.
- If errors are found, feedback is sent back to Gemini.
- Gemini generates an improved version.
- The process continues until the code passes all checks.

---

## Learning Outcome

- Understand Self-Correction AI Agents
- Learn AI code generation
- Learn automatic evaluation
- Learn feedback-based improvement
- Understand Agentic AI workflows

---

## Author

**Esha Jameel**