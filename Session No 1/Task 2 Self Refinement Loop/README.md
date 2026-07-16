# Task 2: Self-Refinement Loop

## Objective

The objective of this task is to understand how an AI model can review and improve its own response. Instead of stopping after generating the first answer, the AI evaluates its output and creates a better, more polished version.

---

## Concepts Covered

- Gemini API Integration
- Prompt Engineering
- Self-Refinement Loop
- AI Self-Critique
- Response Improvement
- Iterative AI Workflow

---

## How It Works

1. Load the Gemini API key from the `.env` file.
2. Create a Gemini client.
3. Ask the AI to generate an initial product description.
4. Store the generated response as the first draft.
5. Send the first draft back to the AI with instructions to review and improve it.
6. The AI analyzes grammar, flow, marketing impact, and professional tone.
7. Display both the original draft and the refined version for comparison.

---

## Workflow

User Topic
↓
Generate First Draft
↓
Review the Draft
↓
Improve the Content
↓
Generate Final Refined Version

---

## Technologies Used

- Python
- Google Gemini API
- python-dotenv

---

## Learning Outcomes

After completing this task, I learned:

- How AI can improve its own responses.
- How iterative prompting produces higher-quality outputs.
- How to compare an initial draft with a refined version.
- How prompt engineering influences the quality of AI-generated content.
- How to build simple AI workflows that refine responses automatically.

---

## Output

The program generates two versions of the same product description:

- Original Draft
- Refined Draft

The refined version is more professional, persuasive, grammatically correct, and better suited for marketing purposes.

---

## Key Takeaway

A Self-Refinement Loop enables an AI model to review, evaluate, and improve its own output, resulting in more accurate and higher-quality responses without changing the underlying model.