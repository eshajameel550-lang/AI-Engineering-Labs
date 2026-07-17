import os
from dotenv import load_dotenv
from google import genai

# ============================================================
# Environment Variables & Gemini Client Setup
# ============================================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please check your .env file.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

# ============================================================
# TASK 2: Modified Few-Shot Prompting
# ============================================================

few_shot_prompt = """
You are an AI Career Mentor who answers students in a simple and motivating way.

Example 1:
Question: What is HTML?
Answer: HTML is the standard markup language used to create web pages.

Example 2:
Question: What is CSS?
Answer: CSS is used to style web pages by controlling colors, fonts, spacing, and layouts.

Example 3:
Question: What is JavaScript?
Answer: JavaScript is a programming language that adds interactivity and dynamic behavior to websites.

Now answer the following question in the same style.

Question: What is Python?

Answer:
"""

response = client.models.generate_content(
    model=MODEL_NAME,
    contents=few_shot_prompt
)

print("=" * 60)
print("TASK 2 : MODIFIED FEW-SHOT PROMPTING")
print("=" * 60)
print(response.text)
print("=" * 60)