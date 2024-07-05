import speech_recognition as sr
recognizer = sr.Recognizer()



def speech_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  # You can use other speech recognition APIs as well
        while text:
            print(f"Text: {text}")
            if text == 'phone':
                break
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")

if __name__ == "__main__":
    speech_to_text()
