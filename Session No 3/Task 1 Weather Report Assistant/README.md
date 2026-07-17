# Task 1 - Weather Report Assistant

## Objective

Build an AI-powered Weather Report Assistant using the Gemini API. The assistant understands user weather queries, simulates function calling, retrieves weather information, and generates a natural language response.

## Features

- Weather Assistant using Gemini AI
- Mock Weather Database
- Function Calling Simulation
- Interactive User Input
- Friendly AI Responses

## Technologies Used

- Python
- Gemini API
- google-generativeai
- python-dotenv

## Project Structure

```
Task 1 Weather Report Assistant/
│── main.py
│── README.md
│── requirements.txt
│── .env
│── output.txt
```

## How to Run

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Add Gemini API Key

Create a `.env` file and add:

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

### 5. Run the Project

```bash
python main.py
```

## Expected Output

- Detects weather-related questions.
- Simulates a function call.
- Retrieves weather information.
- Generates a friendly AI response.

## Author

**Esha Jameel**