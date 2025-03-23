import google.generativeai as gemini
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
gemini.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize the chatbot
def chatbot():
    print("Welcome to the Mental Health Chatbot! Type 'exit' to end the conversation.")
    
    # Initialize the Gemini model
    model = gemini.GenerativeModel('gemini-2.0-flash')
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the chatbot
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Take care.")
            break
        
        # Generate a response using Gemini
        try:
            response = model.generate_content(user_input)
            print(f"Chatbot: {response.text}")
        except Exception as e:
            print(f"Chatbot: Sorry, I encountered an error. Please try again. Error: {e}")

# Run the chatbot
if __name__ == '__main__':
    chatbot()