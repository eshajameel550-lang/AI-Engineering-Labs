import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ============================================================
# Environment Variables & Gemini Client Setup
# ============================================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "ERROR: GOOGLE_API_KEY environment variable mein nahi mila."
    )

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

# ============================================================
# Tool
# ============================================================

def calculate(operation: str, num1: float, num2: float):

    print(f"\n⚡ Tool Running: {operation}")

    if operation == "add":
        return f"The result is {num1 + num2}"

    elif operation == "subtract":
        return f"The result is {num1 - num2}"

    return "Unsupported Operation"


# ============================================================
# Agent Class
# ============================================================

class AgentWithTools:

    def __init__(self):

        self.chat = client.chats.create(

            model=MODEL_NAME,

            config=types.GenerateContentConfig(

                tools=[calculate],

                temperature=0.0

            )

        )

    def handle_query(self, user_message):

        print("\n" + "=" * 60)

        print("User Message:")
        print(user_message)

        print("-" * 60)

        response = self.chat.send_message(user_message)

        print("Agent Response:")
        print(response.text.strip())

        print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("\n--- Running Task 3: Agentic Tool Integration ---")

    math_agent = AgentWithTools()

    math_agent.handle_query("Add 50 and 20")

    time.sleep(2)

    math_agent.handle_query(
        "What is the definition of an AI Agent?"
    )

    print("\nTask 3 Completed Successfully!")