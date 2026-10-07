import pandas as pd

# Load the first row of your dataset to check columns
df = pd.read_csv("crop_production.csv", nrows=1)

print("--- Dataset Columns ---")
print(df.columns.tolist())
