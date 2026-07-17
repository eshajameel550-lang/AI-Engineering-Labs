import os
import subprocess
import tempfile
from dotenv import load_dotenv
import google.generativeai as genai

# ==================================================
# Load API Key
# ==================================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==================================================
# CODER AGENT
# ==================================================

class CoderAgent:

    def __init__(self):
        self.code = ""
        self.attempts = 0

    def write_code(self, task, feedback=None):

        self.attempts += 1

        if feedback:

            prompt = f"""
Task:
{task}

The previous code failed.

Feedback:
{feedback}

Write corrected Python code.

Return ONLY Python code.
"""

        else:

            prompt = f"""
Task:

{task}

Write Python code that:

1. Takes input:
Enter a number:

2. Converts input to integer

3. Calculates square

4. Prints:

The square of NUMBER is SQUARE

Return ONLY Python code.
"""

        response = model.generate_content(prompt)

        code = response.text.strip()

        # Remove Markdown

        if code.startswith("```python"):
            code = code.replace("```python", "").replace("```", "").strip()

        elif code.startswith("```"):
            code = code.replace("```", "").strip()

        self.code = code

        return self.code


# ==================================================
# EVALUATOR
# ==================================================

class EvaluatorAgent:

    def evaluate(self, code):

        errors = []

        # Syntax Check

        try:

            compile(code, "<string>", "exec")

        except SyntaxError as e:

            errors.append(f"Syntax Error : {e}")

        temp_file = None

        try:

            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=".py",
                delete=False
            ) as f:

                f.write(code)

                temp_file = f.name

            result = subprocess.run(

                ["python", temp_file],

                input="5\n",

                capture_output=True,

                text=True,

                timeout=5

            )

            if result.returncode != 0:

                errors.append(result.stderr)

            else:

                output = result.stdout.strip()

                expected = "The square of 5 is 25"

                if expected not in output:

                    errors.append(

                        f"Logic Error\nExpected : {expected}\nGot : {output}"

                    )

        except subprocess.TimeoutExpired:

            errors.append("Program Timeout")

        except Exception as e:

            errors.append(str(e))

        finally:

            if temp_file and os.path.exists(temp_file):

                os.remove(temp_file)

        return errors


# ==================================================
# SELF CORRECTION LOOP
# ==================================================

def run_self_correction():

    task = """
Write a Python program that:

1. Asks the user:

Enter a number:

2. Converts input into integer

3. Calculates square

4. Prints:

The square of NUMBER is SQUARE
"""

    coder = CoderAgent()

    evaluator = EvaluatorAgent()

    feedback = None

    max_attempts = 5

    print("=" * 60)
    print("SELF CORRECTION AI AGENT")
    print("=" * 60)

    print("\nTask:")
    print(task)

    for attempt in range(1, max_attempts + 1):

        print("\n" + "-" * 60)

        print(f"Attempt #{attempt}")

        print("-" * 60)

        print("Generating Code...\n")

        code = coder.write_code(task, feedback)

        print(code)

        print("\nEvaluating...\n")

        errors = evaluator.evaluate(code)

        if not errors:

            print("Code Passed Successfully.")

            break

        else:

            print("Errors Found:")

            for err in errors:

                print("-", err)

            feedback = "\n".join(errors)

            if attempt == max_attempts:

                print("\nMaximum attempts reached.")

    print("\n" + "=" * 60)
    print("FINAL GENERATED CODE")
    print("=" * 60)

    print(coder.code)


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    run_self_correction()