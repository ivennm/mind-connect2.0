import base64
import cv2
import numpy as np
from deepface import DeepFace
from flask import Flask, render_template, request, jsonify
from gemini_backend import generate_response
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if not user_input:
            return render_template('chat.html', error="No input provided")

        # Assuming generate_response is a function that generates a response based on user input
        my_variable = generate_response(user_input)
        return render_template('chat.html', variable=my_variable)

    return render_template('chat.html')  # Handles GET requests and initial page load

# Route to handle emotion detection from the frontend
@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    image_data = data['image_data'].split(',')[1]  # Remove the 'data:image/png;base64,' part
    
    # Decode the base64 image data
    img_data = base64.b64decode(image_data)
    np_arr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    # Analyze the emotion using DeepFace
    try:
        analyze = DeepFace.analyze(frame, actions=['emotion'], silent=True)
        dominant_emotion = analyze[0]['dominant_emotion']
        print(dominant_emotion)
        return render_template('chat.html', emotion=dominant_emotion)  # Handles GET requests and initial page load
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)