import pandas as pd

df = pd.read_csv("dataset/phishing_url_dataset.csv")

print("Columns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())