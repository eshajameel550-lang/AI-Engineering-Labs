import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# ==========================================
# Load API Key
# ==========================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


# ==========================================
# Memory Assistant
# ==========================================

class MemoryAssistant:

    def __init__(self, storage_file="memory.json"):

        self.storage_file = storage_file

        self.memory_data = self.load_memory()

    # --------------------------------------

    def load_memory(self):

        if os.path.exists(self.storage_file):

            with open(self.storage_file, "r", encoding="utf-8") as f:

                return json.load(f)

        return {}

    # --------------------------------------

    def save_memory(self):

        with open(self.storage_file, "w", encoding="utf-8") as f:

            json.dump(self.memory_data, f, indent=4, ensure_ascii=False)

    # --------------------------------------

    def save_preference(self, user_id, preference):

        if user_id not in self.memory_data:

            self.memory_data[user_id] = []

        self.memory_data[user_id].append({

            "content": preference

        })

        self.save_memory()

        return "Preference Saved Successfully."

    # --------------------------------------

    def get_preferences(self, user_id):

        return self.memory_data.get(user_id, [])

    # --------------------------------------

    def ask_with_memory(self, user_id, question):

        memories = self.get_preferences(user_id)

        memory_context = "\n".join(

            [m["content"] for m in memories]

        )

        prompt = f"""
You are a helpful AI Assistant.

User ID:

{user_id}

Previous Memories:

{memory_context if memory_context else "No previous memories."}

Current Question:

{question}

Answer naturally using previous memories.
"""

        try:

            response = model.generate_content(prompt)

            return response.text.strip()

        except Exception as e:

            return f"Gemini Error:\n{e}"


# ==========================================
# MAIN
# ==========================================

assistant = MemoryAssistant()

user_id = "student_001"

print("=" * 60)
print("LONG TERM MEMORY ASSISTANT")
print("=" * 60)

print("\nSaving Preferences...\n")

preferences = [

    "Mujhe Python pasand hai",

    "Mujhe Coding seekhna pasand hai",

    "Mera favourite topic AI hai",

    "Mera naam Ali hai"

]

for pref in preferences:

    print("Saving:", pref)

    print(assistant.save_preference(user_id, pref))

print("\n")

print("=" * 60)

print("MEMORY QUESTIONS")

print("=" * 60)

questions = [

    "Main kya seekhna pasand karta hoon?",

    "Mera naam kya hai?",

    "Mujhe kaunsa topic pasand hai?"

]

for q in questions:

    print("\nUser:", q)

    answer = assistant.ask_with_memory(user_id, q)

    print("Assistant:", answer)

print("\n")

print("=" * 60)
print("INTERACTIVE MODE")
print("=" * 60)

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":

        print("Goodbye!")

        break

    print("\nAssistant:")

    print(assistant.ask_with_memory(user_id, query))