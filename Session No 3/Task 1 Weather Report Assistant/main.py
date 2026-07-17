import os
import re
import time
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
# Weather Tool
# ==========================================

def get_weather(city):
    """Returns mock weather data"""

    weather_data = {
        "paris": "Cloudy, 18°C, Light Rain",
        "london": "Foggy, 12°C, Light Drizzle",
        "karachi": "Hot and Humid, 35°C",
        "tokyo": "Sunny, 25°C",
        "dubai": "Sunny, 42°C",
        "lahore": "Smoggy, 30°C",
        "new york": "Partly Cloudy, 22°C",
        "sydney": "Sunny, 28°C"
    }

    city = city.lower()

    if city in weather_data:
        return f"{city.title()}: {weather_data[city]}"

    return f"{city.title()}: Weather information not available."


# ==========================================
# AI Agent
# ==========================================

def run_agent(user_query):

    print("\n" + "=" * 60)
    print(f"USER : {user_query}")
    print("=" * 60)

    prompt = f"""
You are a Weather Assistant.

Available function:

get_weather(city)

If the user asks about weather,
reply ONLY in this format:

FUNCTION_CALL: get_weather(city="city")

Otherwise answer normally.

User Query:
{user_query}
"""

    try:

        response = model.generate_content(prompt)

        reply = response.text.strip()

    except Exception as e:

        print("\nGemini Error:")
        print(e)

        return

    if "FUNCTION_CALL:" in reply:

        print("\nGemini decided to call the weather tool.")

        match = re.search(r'city=["\']([^"\']+)["\']', reply)

        if match:

            city = match.group(1)

            print(f"\nTool Called : get_weather('{city}')")

            weather = get_weather(city)

            print(f"Tool Output : {weather}")

            final_prompt = f"""
User asked:

{user_query}

Weather Tool Output:

{weather}

Answer naturally in friendly English.
"""

            try:

                final = model.generate_content(final_prompt)

                print("\nAssistant:")

                print(final.text)

            except Exception as e:

                print(e)

        else:

            print("City not found.")

    else:

        print("\nAssistant:")

        print(reply)


# ==========================================
# Main Program
# ==========================================

if __name__ == "__main__":

    print("=" * 60)
    print("WEATHER REPORT ASSISTANT")
    print("=" * 60)

    # Only TWO queries to avoid quota

    queries = [

        "What's the weather in London?",

        "Tell me Karachi weather"

    ]

    for query in queries:

        run_agent(query)

        print("\n" + "-" * 60)

        # wait to reduce quota issues
        time.sleep(5)

    print("\nInteractive Mode")

    while True:

        user = input("\nYou : ")

        if user.lower() == "exit":

            print("Goodbye!")

            break

        run_agent(user)