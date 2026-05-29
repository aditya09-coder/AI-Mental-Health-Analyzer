import librosa
import numpy as np

def analyze_voice(file):

    y, sr = librosa.load(file.file)

    mfcc = librosa.feature.mfcc(
        y=y,
        sr=sr,
        n_mfcc=13
    )

    mfcc_mean = np.mean(mfcc)

    emotion = "Neutral"

    if mfcc_mean < -10:
        emotion = "Sad"

    return {
        "emotion": emotion,
        "voice_score": float(mfcc_mean)
    }
