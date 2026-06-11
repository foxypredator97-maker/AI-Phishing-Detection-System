import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df = pd.read_csv("dataset/phishing_url_dataset.csv")

print(df.head(20))