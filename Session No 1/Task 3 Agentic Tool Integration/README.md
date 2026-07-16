# Task 3: Agentic Tool Integration

## Objective

The objective of this task is to understand how an AI Agent can use external tools to perform specific tasks. Instead of answering everything from its own knowledge, the agent decides when to call a tool and uses the tool's result to answer the user.

---

## Concepts Covered

- Gemini API Integration
- AI Agent
- Tool Calling
- Function Calling
- Agent with Tools
- Chat Session
- Temperature
- Prompt Processing

---

## How It Works

1. Load the Gemini API key from the `.env` file.
2. Create a Gemini client.
3. Define a calculation tool that can perform mathematical operations.
4. Register the tool with the AI Agent.
5. Create a chat session using Gemini.
6. The user sends a query to the agent.
7. If the query requires calculation, the agent automatically calls the tool.
8. If the query is general knowledge, the agent answers directly without using the tool.
9. Display the final response to the user.

---

## Workflow

User Query
↓
AI Agent
↓
Analyze the Request
↓
Need Tool?
↓
Yes → Call Calculation Tool → Return Result
↓
No → Respond Using Gemini Knowledge

---

## Technologies Used

- Python
- Google Gemini API
- python-dotenv
- Function Calling
- Tool Integration

---

## Learning Outcomes

After completing this task, I learned:

- How to create custom tools in Python.
- How to register tools with a Gemini AI Agent.
- How AI decides whether a tool is required.
- The difference between tool-based responses and normal AI responses.
- How chat sessions maintain conversation context.

---

## Output

The program demonstrates two different scenarios:

### Query 1
**User:** Add 50 and 20

- The AI detects that a calculation is needed.
- It calls the `calculate()` tool.
- The tool performs the addition.
- The result is returned to the user.

### Query 2
**User:** What is the definition of an AI Agent?

- No calculation is required.
- The AI answers directly using its own knowledge.
- No external tool is called.

---

## Key Takeaway

An AI Agent does not always rely only on its built-in knowledge. When a task requires a specific capability, such as calculations or database access, it can automatically call the appropriate tool, execute it, and return the result to the user.