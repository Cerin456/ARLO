import cv2

def detect_face_emotion():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    if face_cascade.empty():
        raise IOError("Haar Cascade XML file not loaded")

    cap = cv2.VideoCapture(0)

    # Force camera to open
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        return "Camera not accessible"

    emotion = "Neutral"

    print("📷 Webcam ON — Look at the camera. Press 'Q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        # Flip for mirror view
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(60, 60)
        )

        # Status text
        cv2.putText(
            frame,
            "Scanning Face...",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 255),
            2
        )

        if len(faces) == 0:
            cv2.putText(
                frame,
                "No face detected",
                (20, 65),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

            # Demo emotion logic
            if w * h > 15000:
                emotion = "Happy"
            else:
                emotion = "Sad"

            cv2.putText(
                frame,
                f"Emotion: {emotion}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 0, 0),
                2
            )

        cv2.imshow("🔍 Face Emotion Scanner", frame)

        # VERY IMPORTANT: keeps window alive
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == ord('Q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return emotion
