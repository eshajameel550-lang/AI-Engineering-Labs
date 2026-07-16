import os
import time
from dotenv import load_dotenv
from google import genai

# ============================================================
# Environment Variables & Gemini Client Setup
# ============================================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "ERROR: GOOGLE_API_KEY environment variable mein nahi mila. Kindly .env file check karein."
    )

# Gemini Client
client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

# ============================================================
# TASK 2: SELF-REFINEMENT LOOP
# ============================================================

def run_self_refinement_loop(topic):

    print("\n" + "=" * 60)
    print(f"TASK 2: SELF-REFINEMENT LOOP FOR: '{topic}'")
    print("=" * 60)

    # -------------------------
    # Step 1: Initial Draft
    # -------------------------

    initial_prompt = f"""
Write a professional product description for:

{topic}
"""

    initial_response = client.models.generate_content(
        model=MODEL_NAME,
        contents=initial_prompt
    )

    initial_draft = initial_response.text

    print("\n[STEP 1] ORIGINAL DRAFT")
    print("-" * 40)
    print(initial_draft.strip())
    print("-" * 40)

    # Wait for 2 seconds
    time.sleep(2)

    # -------------------------
    # Step 2: Self Critique
    # -------------------------

    refinement_prompt = f"""
Review the following product description.

Improve:

- Grammar
- Flow
- Marketing Impact
- Professional Tone

Rewrite it to be much more persuasive.

Original Description:

{initial_draft}

Return ONLY the improved version.
"""

    refined_response = client.models.generate_content(
        model=MODEL_NAME,
        contents=refinement_prompt
    )

    refined_output = refined_response.text

    print("\n[STEP 2] REFINED OUTPUT")
    print("-" * 40)
    print(refined_output.strip())
    print("-" * 40)


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("\n--- Running Task 2: Self-Refinement ---")

    topic = "A high-end gaming laptop with RTX 4090"

    run_self_refinement_loop(topic)

    print("\nTask Completed Successfully!")