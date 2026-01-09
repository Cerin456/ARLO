from responses import responses

def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in ["angry", "mad", "furious"]):
        return "anger"
    elif any(word in text for word in ["stress", "pressure", "overwhelmed"]):
        return "stress"
    elif any(word in text for word in ["sad", "down", "unhappy"]):
        return "sad"
    elif any(word in text for word in ["depressed", "hopeless", "empty"]):
        return "depressed"
    elif any(word in text for word in ["happy", "excited", "joy"]):
        return "happy"
    else:
        return "neutral"

def get_response(user_input):
    emotion = detect_emotion(user_input)
    suggestions = responses.get(emotion, responses["default"])
    return emotion, suggestions
