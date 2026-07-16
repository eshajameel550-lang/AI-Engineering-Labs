# Task 4: Flipped Interaction (Travel Planner Agent)

## Objective

The objective of this task is to understand how an AI Agent can control a conversation by asking one question at a time. Instead of giving an immediate answer, the agent gathers the required information first and then provides a personalized travel plan.

---

## Concepts Covered

- Gemini API Integration
- AI Agent
- System Instructions
- Flipped Interaction
- Multi-turn Conversation
- Chat Session
- Personalized Responses
- Context Retention

---

## How It Works

1. Load the Gemini API key from the `.env` file.
2. Create a Gemini client.
3. Define a system instruction for the Travel Planner Agent.
4. Start a chat session using Gemini.
5. The user requests help in planning a trip.
6. The agent asks one clarification question at a time.
7. The user provides answers such as destination, budget, and interests.
8. The agent remembers the previous conversation.
9. After collecting enough information, the agent generates a personalized travel plan.

---

## Workflow

User Wants to Plan a Trip
↓
Travel Planner Agent
↓
Ask One Question
↓
User Replies
↓
Store Conversation Context
↓
Ask Next Question
↓
Collect Enough Information
↓
Generate Personalized Travel Plan

---

## Technologies Used

- Python
- Google Gemini API
- python-dotenv
- Gemini Chat API
- System Instructions

---

## Learning Outcomes

After completing this task, I learned:

- How to create a conversational AI agent.
- How system instructions control an AI agent's behavior.
- How chat sessions maintain conversation history.
- How AI collects information step by step.
- How personalized responses are generated using user inputs.

---

## Output

The program simulates a conversation between the user and a Travel Planner Agent.

Example conversation:

- User wants to plan a trip.
- Agent asks for the destination.
- User provides the destination.
- Agent asks for the budget.
- User provides the budget.
- Agent asks about travel preferences.
- Finally, the agent creates a personalized travel plan.

---

## Key Takeaway

A Flipped Interaction Agent does not answer immediately. Instead, it asks relevant questions, collects enough information, remembers the conversation, and then provides a personalized and accurate response. This approach makes AI assistants more interactive and user-focused.