import pandas as pd
import joblib

from utils.feature_extractor import extract_features

# Load model
model = joblib.load("model/phishing_model.pkl")

# Test URL
url = "https://google.com"

# Extract features
features = extract_features(url)

# Convert to dataframe
df = pd.DataFrame([features])

# Prediction
prediction = model.predict(df)[0]

# Probability
probability = model.predict_proba(df)[0]

print("URL:", url)
print("Prediction:", prediction)
print("Probabilities:", probability)

if prediction == 1:
    print("LEGITIMATE WEBSITE")
else:
    print("PHISHING WEBSITE")