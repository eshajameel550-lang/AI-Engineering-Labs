"""
REACT PROMPTING - Reasoning + Acting
Modified Assignment Solution
"""

import time
from datetime import datetime


class ReActAgent:

    def __init__(self):

        self.tools = {
            "search_web": self.search_web,
            "get_location": self.get_location,
            "get_weather": self.get_weather,

            # NEW TOOLS
            "calculate": self.calculate,
            "translate": self.translate,
            "get_time": self.get_time
        }

# ===================================================
# TOOLS
# ===================================================

    def search_web(self, query):
        print(f" Searching: {query}")
        time.sleep(0.5)

        results = {
            "best restaurants": "Top Restaurants: Kolachi, Okra, Cafe Flo",
            "weather": "32°C, Sunny",
            "flights": "Flight PK-301 is On Time"
        }

        return results.get(query, f"Results found for {query}")


    def get_location(self):
        print(" Detecting Location...")
        return "Karachi, Pakistan"


    def get_weather(self, location):
        print(f" Weather for {location}")
        return f"Weather: 32°C Sunny in {location}"


# ===================================================
# NEW TOOL 1
# ===================================================

    def calculate(self, expression):
        print(f" Calculating: {expression}")

        try:
            result = eval(expression)
            return f"Result: {result}"

        except:
            return "Calculation Error"


# ===================================================
# NEW TOOL 2
# ===================================================

    def translate(self, text):

        print(f" Translating: {text}")

        translations = {
            "hello": "Assalam-o-Alaikum",
            "goodbye": "Khuda Hafiz",
            "thank you": "Shukriya"
        }

        return translations.get(
            text.lower(),
            f"No Translation Found for {text}"
        )


# ===================================================
# CHALLENGE TOOL
# ===================================================

    def get_time(self, dummy=None):

        print(" Getting Current Time...")

        return datetime.now().strftime("%I:%M %p")


# ===================================================
# REACT LOOP
# ===================================================

    def run(self, goal):

        print("\n" + "="*60)

        print(f" GOAL: {goal}")

        print("="*60)

        thought = f"I need to complete: {goal}"

        iteration = 0

        while iteration < 4:

            iteration += 1

            print(f"\nStep {iteration}")

            print("-"*30)

            print(f" THOUGHT: {thought}")

# -------------------------
# ACTION
# -------------------------

            if "restaurant" in goal.lower():

                action = "search_web best restaurants"

            elif "weather" in goal.lower():

                location = self.get_location()

                action = f"get_weather {location}"

            elif "flight" in goal.lower():

                action = "search_web flights"

            elif "calculate" in goal.lower():

                action = "calculate 25+30"

            elif "translate" in goal.lower():

                action = "translate hello"

            elif "time" in goal.lower():

                action = "get_time"

            else:

                action = "COMPLETE"

            if action == "COMPLETE":

                print(" GOAL ACHIEVED!")

                return thought

            print(f" ACTION: {action}")

# -------------------------
# Execute Tool
# -------------------------

            if " " in action:

                tool_name, param = action.split(" ", 1)

                observation = self.tools[tool_name](param)

            else:

                observation = self.tools[action]()

# -------------------------
# OBSERVE
# -------------------------

            print(f" OBSERVATION: {observation}")

            thought = f"Based on '{observation}', I can complete the goal."

        return "Goal Completed"


# ===================================================
# RUN DEMO
# ===================================================

print(" REACT AGENT DEMO\n")

goals = [

    "Find best restaurants in the city",

    "Check today's weather",

    "Calculate 25 + 30",

    "Translate hello to Urdu",

    "Check flight status",

    "Get current time"

]

for goal in goals:

    agent = ReActAgent()

    result = agent.run(goal)

    print(f"\n FINAL RESULT: {result}")

    print("="*60)

print("\nThought → Action → Observation = ReAct Agent")