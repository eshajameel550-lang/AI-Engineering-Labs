# Task 1: Persona Expansion Class

## Objective

The objective of this task is to understand how an AI Agent can change its behavior by using different personas. Instead of giving the same answer every time, the AI responds according to a specific role, tone, style, and constraints.

---

## Concepts Covered

- Gemini API Integration
- Environment Variables (.env)
- AI Agent Persona
- Prompt Engineering
- Class and Object (OOP)
- Dynamic Prompt Generation

---

## How It Works

1. Load the Gemini API key from the `.env` file.
2. Create a Gemini client.
3. Define a `PersonaAgent` class.
4. Store multiple personas inside a dictionary.
5. Select a persona based on the given role.
6. Build a prompt using the selected persona.
7. Send the prompt to the Gemini model.
8. Display the AI response.
9. Repeat the process for different personas.

---

## Personas Used

### Critic
- Harsh and judgmental tone.
- Focuses only on weaknesses.
- Never gives praise.

### Writer
- Creative and artistic tone.
- Uses storytelling and metaphors.
- Avoids plain answers.

---

## Technologies Used

- Python
- Google Gemini API
- python-dotenv

---

## Learning Outcomes

After completing this task, I learned:

- How to connect Python with Gemini API.
- How environment variables improve security.
- How AI personas change the model's responses.
- How prompts can control AI behavior.
- How classes can be used to build reusable AI agents.

---

## Output

The same question is answered by two different AI personas:

- Harsh Critic
- Creative Writer

This demonstrates how prompt engineering can significantly change the AI's behavior without changing the model itself.