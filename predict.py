import joblib
import pandas as pd

# Load model
model = joblib.load("model/phishing_model.pkl")

# Example website features
sample = {
    "url_length": 73,
    "valid_url": 0,
    "at_symbol": 0,
    "sensitive_words_count": 0,
    "path_length": 52,
    "isHttps": 0,
    "nb_dots": 5,
    "nb_hyphens": 0,
    "nb_and": 0,
    "nb_or": 0,
    "nb_www": 0,
    "nb_com": 1,
    "nb_underscore": 0
}

df = pd.DataFrame([sample])

prediction = model.predict(df)

if prediction[0] == 1:
    print("⚠️ PHISHING WEBSITE DETECTED")
else:
    print("✅ LEGITIMATE WEBSITE")