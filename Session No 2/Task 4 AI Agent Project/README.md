# Task 8 - AI Resume Parser with JSON Output

## Objective

Build an AI-powered Resume Parser using the Gemini API that extracts information from a resume and returns it in structured JSON format.

## Features

- Extracts resume information using Gemini AI
- Returns valid JSON output
- Parses the following fields:
  - Name
  - Email
  - Phone
  - City
  - Skills
  - Experience
  - Education

## Technologies Used

- Python
- Gemini API
- google-genai
- python-dotenv
- JSON

## Project Structure

```
Task 8 - AI Resume Parser/
│── main.py
│── README.md
│── output.txt
│── .env
```

## How to Run

1. Activate the virtual environment.
2. Install dependencies:
   ```bash
   pip install google-genai python-dotenv