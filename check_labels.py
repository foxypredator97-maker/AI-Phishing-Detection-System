import pandas as pd

df = pd.read_csv("dataset/phishing_url_dataset.csv")

print(df["target"].value_counts())