from utils.feature_extractor import extract_features
from utils.trust_score import calculate_trust_score

url = "https://secure-paypal-login.xyz"

features = extract_features(url)

score = calculate_trust_score(features)

print("Features:")
print(features)

print("\nTrust Score:")
print(score)