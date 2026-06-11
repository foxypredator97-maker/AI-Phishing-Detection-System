import joblib
import pandas as pd

from utils.feature_extractor import extract_features
from utils.trust_score import calculate_trust_score

# Load model
model = joblib.load("model/phishing_model.pkl")

# Test URL
url = "https://paypal-secure-login.xyz"

# Extract features
features = extract_features(url)

# Convert to DataFrame
df = pd.DataFrame([features])

# Predict
prediction = model.predict(df)[0]

# Trust Score
score = calculate_trust_score({
    "url_length": features["url_length"],
    "https": features["isHttps"],
    "has_at": features["at_symbol"],
    "dot_count": features["nb_dots"],
    "suspicious_keywords": features["sensitive_words_count"],
    "has_hyphen": features["nb_hyphens"]
})

print("\nURL:", url)

if prediction == 1:
    print("⚠️ PHISHING WEBSITE DETECTED")
else:
    print("✅ LEGITIMATE WEBSITE")

print("Trust Score:", score, "/100")