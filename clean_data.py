import pandas as pd
import numpy as np

print("⏳ Loading raw agricultural data...")
df = pd.read_csv("crop_production.csv")

# 1. Handle Missing Values
# In this specific dataset, non-reported values are filled with -1. 
# We replace -1 with 0 or NaN so it doesn't mess up statistical averages.
print("🧹 Cleaning missing values and placeholders...")
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].replace(-1, 0)

# 2. Standardize Text Formatting
# Convert names to clean title case and strip any hidden accidental spaces
print("🔤 Standardizing state and district names...")
df['State Name'] = df['State Name'].str.strip().str.title()
df['Dist Name'] = df['Dist Name'].str.strip().str.title()

# Save the polished data as a new clean file
output_file = "crop_production_clean.csv"
df.to_csv(output_file, index=False)
print(f"🎉 Cleaning complete! Saved cleaned dataset as '{output_file}' ({len(df)} records).")
