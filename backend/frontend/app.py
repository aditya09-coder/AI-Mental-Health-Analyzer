import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Explainable AI Mental Health Platform")

menu = st.sidebar.selectbox(
    "Choose Analysis",
    [
        "Text Analysis",
        "Voice Analysis",
        "Face Analysis"
    ]
)

# ---------------- TEXT ANALYSIS ----------------

if menu == "Text Analysis":

    st.header("Text Emotion Detection")

    user_text = st.text_area(
        "Enter your thoughts"
    )

    if st.button("Analyze Text"):

        response = requests.post(
            f"{API_URL}/analyze-text",
            json={"text": user_text}
        )

        result = response.json()

        st.success("Analysis Complete")

        st.write("Sentiment:", result["sentiment"])
        st.write("Confidence:", result["confidence"])
        st.write(
            "Depression Risk:",
            result["depression_risk"]
        )

# ---------------- VOICE ANALYSIS ----------------

if menu == "Voice Analysis":

    st.header("Voice Emotion Detection")

    audio_file = st.file_uploader(
        "Upload Audio File",
        type=["wav", "mp3"]
    )

    if audio_file:

        response = requests.post(
            f"{API_URL}/analyze-voice",
            files={"file": audio_file}
        )

        result = response.json()

        st.success("Voice Analysis Complete")

        st.write("Emotion:", result["emotion"])
        st.write(
            "Voice Score:",
            result["voice_score"]
        )

# ---------------- FACE ANALYSIS ----------------

if menu == "Face Analysis":

    st.header("Facial Emotion Detection")

    image_file = st.file_uploader(
        "Upload Face Image",
        type=["jpg", "png", "jpeg"]
    )

    if image_file:

        response = requests.post(
            f"{API_URL}/analyze-face",
            files={"file": image_file}
        )

        result = response.json()

        st.success("Face Analysis Complete")

        st.write(
            "Faces Detected:",
            result["faces_detected"]
        )

        st.write(
            "Emotion:",
            result["emotion"]
        )
