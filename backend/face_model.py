import cv2
import numpy as np

def analyze_face(file):

    contents = file.file.read()

    np_array = np.frombuffer(contents, np.uint8)

    image = cv2.imdecode(
        np_array,
        cv2.IMREAD_COLOR
    )

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(
        gray,
        1.1,
        4
    )

    emotion = "Neutral"

    if len(faces) > 0:
        emotion = "Possible Stress Detected"

    return {
        "faces_detected": len(faces),
        "emotion": emotion
    }
