import streamlit as st
from face_emotion import detect_face_emotion
try:
    import speech_recognition as sr
    VOICE_AVAILABLE = True
except:
    VOICE_AVAILABLE = False


# ================= SOLUTION ENGINE =================
def get_solution(emotion, user_text=""):
    emotion = emotion.lower()

    if "sad" in emotion or "depress" in emotion:
        return [
            "💙 It's okay to feel sad. You are not weak.",
            "🌿 Try slow breathing: inhale 4s, exhale 6s.",
            "📝 Write down one small thing you're grateful for.",
            "📞 Consider talking to someone you trust."
        ]

    elif "stress" in emotion or "anxious" in emotion:
        return [
            "🌊 Pause for a moment and unclench your body.",
            "🧘 Try the 5-4-3-2-1 grounding exercise.",
            "☕ Drink some water and slow down your breath.",
            "🗂 Break tasks into very small steps."
        ]

    elif "angry" in emotion:
        return [
            "🔥 Anger is a signal, not a failure.",
            "🚶 Step away from the trigger for 5 minutes.",
            "📝 Write what you feel without filtering.",
            "💨 Release tension with slow exhalation."
        ]

    elif "happy" in emotion:
        return [
            "😊 Enjoy this moment fully.",
            "🌞 Share your positivity with someone.",
            "📔 Capture this feeling in a journal."
        ]

    else:
        return [
            "🌼 Take a slow breath and check in with yourself.",
            "🧘 Be present — you are safe right now.",
            "✨ Small steps still matter."
        ]


# ================= TEXT EMOTION DETECTION =================
def detect_text_emotion(text):
    text = text.lower()

    if "sad" in text or "depress" in text or "hopeless" in text:
        return "sad"
    elif "stress" in text or "anxious" in text or "worried" in text:
        return "stress"
    elif "angry" in text or "mad" in text:
        return "angry"
    elif "happy" in text or "good" in text:
        return "happy"
    else:
        return "neutral"


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Arlo – Mental Wellness",
    page_icon="🌈",
    layout="centered"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0B132B, #1C2541);
}
.title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #EAF6FF;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #CDE7F0;
    margin-bottom: 30px;
}
.card {
    background-color: #FAFAFA;
    padding: 35px;
    border-radius: 24px;
    box-shadow: 0px 15px 35px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}
.card h3 {
    color: #1F3C88;
    font-size: 26px;
}
.card p {
    color: #2C3E50;
    font-size: 18px;
    line-height: 1.7;
}
.section-title {
    color: #EAF6FF;
    font-size: 22px;
    margin-top: 30px;
}
.footer {
    text-align: center;
    color: #BFD7EA;
    margin-top: 40px;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<div class='title'>🌈 Arlo</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your AI Companion for Mental Wellness</div>", unsafe_allow_html=True)

# ================= HOPE CARD =================
st.markdown("""
<div class="card">
    <h3>✨ You are not alone</h3>
    <p>
        Arlo is here to help you understand your emotions and gently guide you
        toward calmness, hope, and clarity.
    </p>
    <p>
        🌱 Take a deep breath<br>
        💙 Relax your mind<br>
        😊 Let Arlo support you
    </p>
</div>
""", unsafe_allow_html=True)

# ================= TEXT INPUT =================
st.markdown("<div class='section-title'>📝 Share your thoughts</div>", unsafe_allow_html=True)

user_text = st.text_area(
    "Type how you are feeling:",
    placeholder="I feel anxious today... I am stressed... I feel hopeful..."
)

if user_text:
    st.success("💬 Thank you for opening up. Your feelings matter.")

    text_emotion = detect_text_emotion(user_text)

    st.markdown("### 🧩 Arlo’s Support Suggestions")
    solutions = get_solution(text_emotion, user_text)

    for step in solutions:
        st.write(step)

# ================= VOICE INPUT =================
st.markdown("<div class='section-title'>🎤 Or speak your feelings</div>", unsafe_allow_html=True)

voice_text = ""

if st.button("🎙️ Record Voice"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎧 Listening... please speak")
        audio = recognizer.listen(source)

    try:
        voice_text = recognizer.recognize_google(audio)
        st.success("🗣️ You said:")
        st.write(voice_text)

        voice_emotion = detect_text_emotion(voice_text)
        solutions = get_solution(voice_emotion, voice_text)

        st.markdown("### 🧩 Arlo’s Support Suggestions")
        for step in solutions:
            st.write(step)

    except:
        st.error("❌ Sorry, I couldn’t understand. Please try again.")

# ================= CAMERA EMOTION SCAN =================
st.markdown("<div class='section-title'>📷 Emotion Detection</div>", unsafe_allow_html=True)

if st.button("💫 Start Emotion Scan"):
    st.info("📷 Webcam will open. Press 'Q' to finish scanning.")
    emotion = detect_face_emotion()

    st.success(f"🧠 Detected Emotion: **{emotion}**")

    solutions = get_solution(emotion, user_text + " " + voice_text)

    st.markdown("### 🧩 Suggested Support Steps")
    for step in solutions:
        st.write(step)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
    ✨ Small steps today can lead to a brighter tomorrow ✨
</div>
""", unsafe_allow_html=True)
