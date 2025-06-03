# cadenzacdz.github.io
# BukuWarung AI Pitch Generator Prototype

This is a 2-day prototype built for the BukuWarung AI Prototype Challenge. It demonstrates an AI-powered solution to help sales agents generate personalized pitches for merchants.

## Problem Addressed
Sub-optimal Sales Process: Current canvassing and sales pitching methods result in low conversion rates. This tool aims to provide more tailored and effective pitches.

## Features
- Select Merchant Business Type.
- Select Primary Product Interest / Focus.
- Input Observed Merchant Challenge / Pain Point.
- Generates a personalized sales pitch in Bahasa Indonesia using OpenAI's GPT model.
- Simple, clean, and mobile-friendly web interface.

## Technical Stack
- **Backend:** Python (Flask)
- **AI API:** OpenAI GPT-3.5 Turbo (or newer)
- **Frontend:** HTML, CSS, JavaScript (Vanilla)

## Setup & Running Locally

1.  **Prerequisites:**
    * Python 3.7+ installed
    * An OpenAI API Key

2.  **Clone the repository (if applicable) or create the files as described.**

3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your OpenAI API Key:**
    * Create a file named `.env` in the root directory of the project.
    * Add your OpenAI API key to it like this:
        ```
        OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"
        ```
    * Replace `"YOUR_OPENAI_API_KEY_HERE"` with your actual key.

6.  **Run the Flask application:**
    ```bash
    python app.py
    ```

7.  Open your web browser and go to `http://127.0.0.1:5001/` (or the port specified in `app.py`).

## Deployment
This application is a simple Flask app and can be deployed to various platforms that support Python WSGI applications, such as:
- PythonAnywhere
- Heroku
- Google Cloud Run
- AWS Elastic Beanstalk
- DigitalOcean App Platform

Ensure your `OPENAI_API_KEY` is set as an environment variable on the deployment platform.

## Business Value
- **Improved Pitch Relevance:** AI generates pitches tailored to specific merchant profiles and needs.
- **Increased Sales Agent Efficiency:** Reduces time spent manually crafting pitches.
- **Potentially Higher Conversion Rates:** More relevant pitches are more likely to resonate with merchants.
- **Scalable Sales Support:** Provides a consistent quality of pitch across a sales team.

## AI Integration
- Uses the OpenAI API (`gpt-3.5-turbo` or newer) for natural language generation.
- Prompt engineering is used to guide the AI to produce relevant and persuasive sales pitches in Bahasa Indonesia, tailored to BukuWarung's MSME segment.