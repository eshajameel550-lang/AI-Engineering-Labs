import os
import json
from dotenv import load_dotenv
from google import genai

# ==========================================
# Load API Key
# ==========================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL_NAME = "gemini-2.5-flash"

print("=" * 60)
print("AI RESUME PARSER")
print("=" * 60)

# ==========================================
# Sample Resume
# ==========================================

resume = """
Name: Esha Jameel
Email: esha@email.com
Phone: 0300-1234567
City: Khanewal
Skills: Python, HTML, CSS, AI, JavaScript
Experience: Frontend Developer Intern
Education: Intermediate (ICS)
"""

print(resume)

# ==========================================
# Prompt
# ==========================================

prompt = f"""
Extract the following resume into JSON.

Resume:

{resume}

Return ONLY valid JSON.

Required Keys:

name
email
phone
city
skills
experience
education
"""

# ==========================================
# Gemini
# ==========================================

response = client.models.generate_content(
    model=MODEL_NAME,
    contents=prompt
)

text = response.text.strip()

# remove markdown

if text.startswith("```json"):
    text = text.replace("```json", "").replace("```", "").strip()

elif text.startswith("```"):
    text = text.replace("```", "").strip()

# ==========================================
# Convert JSON
# ==========================================

data = json.loads(text)

print("\nFormatted JSON\n")

print(json.dumps(data, indent=4))