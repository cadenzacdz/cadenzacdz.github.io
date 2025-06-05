import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from openai import OpenAI # Make sure you have the latest openai package
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)

# Initialize OpenAI client
# It will automatically pick up the OPENAI_API_KEY from the environment
try:
    client = OpenAI()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    client = None # Set client to None if initialization fails

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pitch', methods=['POST'])
def generate_pitch_route():
    if not client:
        return jsonify({"error": "OpenAI client not initialized. Check API key."}), 500

    try:
        data = request.get_json()
        merchant_type = data.get('merchant_type', 'a small business')
        product_interest = data.get('product_interest', 'BukuWarung digital tools')
        challenge = data.get('challenge', 'growing their business')

        prompt = f"""
        You are a friendly and expert sales assistant for BukuWarung, a company that provides digital solutions to help Micro, Small, and Medium Enterprises (MSMEs) in Indonesia succeed.

        A sales agent is about to talk to a merchant with the following profile:
        - Business Type: {merchant_type}
        - Primary Interest/Need: {product_interest}
        - Observed Challenge: {challenge}

        Generate a concise, persuasive, and friendly sales pitch in Bahasa Indonesia (maximum 3 paragraphs, about 100-150 words).
        The pitch should:
        1. Acknowledge the merchant's business type and their challenge.
        2. Clearly explain how a specific BukuWarung feature or {product_interest} can directly solve their {challenge}.
        3. Emphasize the benefits like ease of use, time-saving, increased profit, or better management for their specific {merchant_type}.
        4. End with a soft call to action, like trying it out or learning more.

        Make the language simple, relatable, and encouraging for an MSME owner.
        """

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access and prefer it
            messages=[
                {"role": "system", "content": "You are a helpful sales assistant for BukuWarung generating sales pitches in Bahasa Indonesia."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=250
        )

        pitch = completion.choices[0].message.content.strip()
        return jsonify({"pitch": pitch})

    except Exception as e:
        print(f"Error during pitch generation: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # For development, you can run with debug=True
    # For deployment, use a proper WSGI server like Gunicorn or Waitress
    app.run(debug=True, port=5001) # Using port 5001 to avoid conflicts if 5000 is in use