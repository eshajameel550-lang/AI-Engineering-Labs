import os
from dotenv import load_dotenv
from google import genai

# ============================================================
# Environment Variables & Gemini Client Setup
# ============================================================

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-2.5-flash"

# ============================================================
# TASK 5: Chain Of Thoughts  Prompting
# ============================================================

# Problems
problems = [
    "What is 15% of 200?",
    "If 5 apples cost 50 rupees, what do 8 apples cost?",
    "A square has side 6 cm. What is its area?"
]

for i, problem in enumerate(problems, start=1):

    print("=" * 60)
    print(f"Problem {i}: {problem}")

    # WITHOUT CoT (Direct Answer)
    prompt1 = f"""
Answer the following question directly.
Do not explain the steps.

Question:
{problem}
"""

    response1 = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt1
    )

    print("\nWITHOUT CoT")
    print(response1.text)

    # WITH STEP-BY-STEP EXPLANATION
    prompt2 = f"""
Solve the following problem.
Give a brief step-by-step explanation and then the final answer.

Question:
{problem}
"""

    response2 = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt2
    )

    print("\nWITH STEP-BY-STEP")
    print(response2.text)