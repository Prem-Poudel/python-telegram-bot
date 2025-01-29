# utils.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_TOKEN'))

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
