# utils.py
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

def connect_to_gemini():
    """Connect to Gemini API."""
    try:
        genai.configure(api_key=os.getenv('GEMINI_TOKEN'))
        return True
    except Exception as e:
        print(f"Error connecting to Gemini API: {e}")
        return False

def validate_connection():
    """Validate connection to Gemini API."""
    if connect_to_gemini():
        print("Connected to Gemini API.")
    else:
        print("Unable to connect to Gemini API.")

validate_connection()



# Configure Gemini API
def generate_description(content):
    """Generates description using Gemini API."""
    system_instruction = 'You are a assistant that assists users with their queries. Your name is JARVIS. Jarvis stands for Just A Rather Very Intelligent System.'
    try:
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=system_instruction
            )
        response = model.generate_content(content)
        
        if response and hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "No description generated."
    except Exception as e:
        print(f"Error generating description: {e}")
        return "Unable to generate description."
