import speech_recognition as sr
import pyttsx3
import os

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
    return 

def output_text(text):
    file_path = 'output.txt'
    if os.path.exists(file_path):
        with open('output.txt', 'w') as file:
            file.write(text)
            file.write('\n')
    else:
        with open('output.txt', 'a') as file:
            file.write(text)
            file.write('\n')

    return

while(1):
    text = record_text()
    output_text(text)
    print("Finished Writing text")