import pandas as pd
import sqlite3

print("⏳ Loading cleaned CSV file...")
df = pd.read_csv("crop_production_clean.csv")

# Clean column names for SQL (replace spaces and brackets with underscores)
df.columns = df.columns.str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

print("💾 Connecting to SQLite database (agridata.db)...")
conn = sqlite3.connect("agridata.db")

# Save to a database table named 'crop_data'
df.to_sql(name="crop_data", con=conn, if_exists="replace", index=False)
conn.close()

print("🎉 SQL Database 'agridata.db' created successfully with 'crop_data' table!")
