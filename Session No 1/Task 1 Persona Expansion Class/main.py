import os
import time
from dotenv import load_dotenv
from google import genai
print("Program Started")

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
# TASK 1: Persona Expansion Class
# ============================================================

class PersonaAgent:

    def __init__(self, role):
        self.role = role

        self.personas = {

            "critic": {
                "role": "Harsh Critic",
                "tone": "Harsh, judgmental, and highly critical",
                "style": "Analytical, pointing out flaws and imperfections instantly",
                "constraints": "Do not praise anything, focus entirely on shortcomings and weaknesses."
            },

            "writer": {
                "role": "Creative Writer",
                "tone": "Imaginative, expressive, and artistic",
                "style": "Rich story-like formatting, heavy use of metaphors and vivid poetry",
                "constraints": "Avoid direct/plain answers, express the core truth through art or storytelling."
            }

        }

    def respond(self, question):

        persona = self.personas[self.role]

        print("\n" + "=" * 50)
        print(f"ROLE: {persona['role']} | TONE: {persona['tone']}")
        print("-" * 50)

        prompt = f"""
You are a {persona['role']}.

Your tone: {persona['tone']}

Your style: {persona['style']}

Constraints:
{persona['constraints']}

Question:
{question}

Respond strictly in character based on the rules above.
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        print(f"Q: {question}")
        print(f"A: {response.text.strip()}")
        print("=" * 50)

        return response.text


# ============================================================
# Execute Task 1
# ============================================================

if __name__ == "__main__":

    print("\n--- Running Task 1: Persona Expansion ---")

    question = "What do you think about the rapidly growing trend of AI automation?"

    for role in ["critic", "writer"]:
        agent = PersonaAgent(role)
        agent.respond(question)
        time.sleep(2)