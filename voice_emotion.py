import speech_recognition as sr

def detect_voice_emotion():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio).lower()

        if any(w in text for w in ["angry", "mad"]):
            return "anger"
        elif any(w in text for w in ["sad", "down"]):
            return "sad"
        elif any(w in text for w in ["stress", "pressure"]):
            return "stress"
        elif any(w in text for w in ["happy", "excited"]):
            return "happy"
        else:
            return "neutral"

    except:
        return "neutral"
