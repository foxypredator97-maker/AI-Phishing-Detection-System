from flask import Flask, render_template, request
import pandas as pd
import joblib

from utils.feature_extractor import extract_features
from utils.trust_score import calculate_trust_score

app = Flask(__name__)

# Load trained model
model = joblib.load("model/phishing_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    url = request.form["url"]

    # Extract URL features
    features = extract_features(url)

    # Convert to DataFrame
    df = pd.DataFrame([features])

    # AI Prediction
    prediction = model.predict(df)[0]

    # Trust Score
    score = calculate_trust_score(features)

    # Risk Level
    if score >= 85:
        risk = "LOW"
    elif score >= 60:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    # AI Result
    if prediction == 1:
        result = "PHISHING WEBSITE"
    else:
        result = "LEGITIMATE WEBSITE"

    # Final Security Verdict
    if score >= 85:
        verdict = "SAFE"
    elif score >= 60:
        verdict = "SUSPICIOUS"
    else:
        verdict = "PHISHING"

    return render_template(
        "index.html",
        url=url,
        result=result,
        score=score,
        risk=risk,
        verdict=verdict
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)