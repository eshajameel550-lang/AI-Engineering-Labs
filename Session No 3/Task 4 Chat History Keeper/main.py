import os
from dotenv import load_dotenv
import google.generativeai as genai

# ==========================================
# Load API Key
# ==========================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================================
# Chat History
# ==========================================

messages = []

print("=" * 60)
print("CHAT HISTORY KEEPER")
print("=" * 60)

questions = [

    "What is your name?",

    "What are you interested in?",

    "What is your favourite topic?"

]

for question in questions:

    print(f"\nAssistant: {question}")

    user_input = input("You: ")

    messages.append({

        "role": "user",

        "content": user_input

    })

    memory = ""

    for msg in messages:

        if msg["role"] == "user":

            memory += f"User said: {msg['content']}\n"

    prompt = f"""
You are a friendly AI assistant.

Remember everything the user tells you.

Conversation History:

{memory}

Current User Message:

{user_input}

Reply naturally and show that you remember previous information.
"""

    response = model.generate_content(prompt)

    answer = response.text.strip()

    messages.append({

        "role": "assistant",

        "content": answer

    })

    print("\nAssistant:")

    print(answer)

# ==========================================
# Memory Test
# ==========================================

print("\n" + "=" * 60)

print("MEMORY TEST")

print("=" * 60)

test_prompt = f"""
Based on the complete conversation below,

Answer:

1. What is the user's name?

2. What is the user's interest?

3. What is the user's favourite topic?

Conversation:

{messages}
"""

response = model.generate_content(test_prompt)

print("\nAssistant Summary:\n")

print(response.text)