from fastapi import FastAPI, UploadFile, File
from text_model import analyze_text
from voice_model import analyze_voice
from face_model import analyze_face

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mental Health AI API Running"}

# ---------------- TEXT ANALYSIS ----------------

@app.post("/analyze-text")
async def analyze_text_api(data: dict):

    text = data["text"]

    result = analyze_text(text)

    return result

# ---------------- VOICE ANALYSIS ----------------

@app.post("/analyze-voice")
async def analyze_voice_api(file: UploadFile = File(...)):

    result = analyze_voice(file)

    return result

# ---------------- FACE ANALYSIS ----------------

@app.post("/analyze-face")
async def analyze_face_api(file: UploadFile = File(...)):

    result = analyze_face(file)

    return result
