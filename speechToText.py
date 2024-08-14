import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()

def speech_to_text():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1) 
        print("Speak something...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        try:
            text = recognizer.recognize_google(audio)
            print(f"Original Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
    return None

def translate_text(text, dest_lang='hi'):
    try:
        translation = translator.translate(text, dest=dest_lang)
        print(f"Translated Text ({dest_lang}): {translation.text}")
    except Exception as e:
        print(f"Translation Error: {e}")

if __name__ == "__main__":
   
    text = speech_to_text()
    
    if text:
        
        translate_text(text, dest_lang='hi')
