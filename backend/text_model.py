from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_text(text):

    prediction = classifier(text)

    label = prediction[0]["label"]
    score = prediction[0]["score"]

    depression_risk = "Low"

    if label == "NEGATIVE" and score > 0.80:
        depression_risk = "Moderate"

    return {
        "input_text": text,
        "sentiment": label,
        "confidence": round(score * 100, 2),
        "depression_risk": depression_risk
    }
