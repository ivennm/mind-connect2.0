import google.generativeai as gemini
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
gemini.configure(api_key=os.getenv('GEMINI_API_KEY'))
print("gemini_backend.py is being executed")

# Function to generate a response
def generate_response(user_input):
    print("generate_response function is being called")
    try:
        # Initialize the Gemini model
        model = gemini.GenerativeModel('gemini-2.0-flash')
        # Generate a response
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"
