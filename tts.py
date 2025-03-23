import pyttsx3
import time

# Initialize the converter
engine = pyttsx3.init()
# Set speech rate (slower)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Decrease rate to make it slower

# Set volume (optional, default is 1.0)
engine.setProperty('volume', 1)  # Adjust volume between 0.0 and 1.0 (1.0 is max)

# Set voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  

def speak():
    # Convert text to speech
    while True:
        with open('output.txt', 'r') as file:
            text = file.read().strip()

            if key in text:
                time.sleep(1)
                continue

            if text:
                engine.say(text)
                engine.runAndWait()
                with open('output.txt', 'a') as file:
                    file.write(f'\n{key}')
            time.sleep(1)
    return

key = '!@#$%^&*()_+!!!44444444!!!!!-=[]|;:,.<>?/~'
speak()


# Open and read the text file
# The text file will be updated for every response from the therapist

##### TEST CODE #####
# with open('output.txt', 'r') as file:
#     text = file.read()

# # Convert text to speech
# engine.say(text)
# engine.runAndWait()
