import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def speech_to_text(language='en-IN'):
    

    # Capture speech using microphone
    with sr.Microphone() as source:
        print(f"Listening... (Language: {language})")
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio, language=language)
            print(f"Text: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")


if __name__ == "__main__":
    print("Choose Language:")
    print("1. English (India)")
    print("2. Hindi")
    print("3. Japanese")
    print("4. Spanish")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        speech_to_text('en-IN')
    elif choice == '2':
        speech_to_text('hi-IN')
    elif choice == '3':
        speech_to_text('ja-JP')
    elif choice == '4':
        speech_to_text('es-ES')
    else:
        print("Invalid choice.")
