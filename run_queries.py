import sqlite3
import pandas as pd

# Open a secure connection to our SQLite database file
conn = sqlite3.connect("agridata.db")
print("🔌 Database connected successfully!")

# -------------------------------------------------------------
# QUESTION 1: Find year-wise trends for the top 3 rice states
# -------------------------------------------------------------
print("\n📊 --- Query 1: Top 3 States Rice Production Trends ---")

query_1 = """
    SELECT State_Name, Year, SUM(RICE_PRODUCTION_1000_tons) as Total_Rice
    FROM crop_data
    WHERE State_Name IN (
        SELECT State_Name 
        FROM crop_data 
        GROUP BY State_Name 
        ORDER BY SUM(RICE_PRODUCTION_1000_tons) DESC 
        LIMIT 3
    )
    GROUP BY State_Name, Year
    ORDER BY State_Name, Year DESC
    LIMIT 10;
"""

df1 = pd.read_sql(query_1, conn)
print(df1)

# -------------------------------------------------------------
# QUESTION 2: Top 5 Districts by Wheat Yield Increase (Last 5 Years)
# -------------------------------------------------------------
print("\n📊 --- Query 2: Top 5 Districts Wheat Yield Increase ---")

query_2 = """
    SELECT Dist_Name, State_Name, 
           (MAX(WHEAT_YIELD_Kg_per_ha) - MIN(WHEAT_YIELD_Kg_per_ha)) as Yield_Increase
    FROM crop_data
    WHERE Year >= (SELECT MAX(Year) - 5 FROM crop_data)
    GROUP BY Dist_Name, State_Name
    ORDER BY Yield_Increase DESC
    LIMIT 5;
"""

df2 = pd.read_sql(query_2, conn)
print(df2)


# -------------------------------------------------------------
# QUESTION 3: States with the Highest Growth in Oilseed Production
# -------------------------------------------------------------
print("\n📊 --- Query 3: Top States Oilseed Production Growth ---")

query_3 = """
    SELECT State_Name, 
           (SUM(CASE WHEN Year = (SELECT MAX(Year) FROM crop_data) THEN OILSEEDS_PRODUCTION_1000_tons ELSE 0 END) - 
            SUM(CASE WHEN Year = (SELECT MAX(Year) - 5 FROM crop_data) THEN OILSEEDS_PRODUCTION_1000_tons ELSE 0 END)) as Five_Year_Growth
    FROM crop_data
    GROUP BY State_Name
    ORDER BY Five_Year_Growth DESC
    LIMIT 5;
"""

df3 = pd.read_sql(query_3, conn)
print(df3)

# -------------------------------------------------------------
# QUESTION 4: District-wise Correlation Metrics (Area vs Production)
# -------------------------------------------------------------
print("\n📊 --- Query 4: District-wise Crop Production Ratios ---")

query_4 = """
    SELECT Dist_Name, State_Name, 
           ROUND((RICE_PRODUCTION_1000_tons / (RICE_AREA_1000_ha + 0.001)), 2) as Rice_Yield_Ratio,
           ROUND((WHEAT_PRODUCTION_1000_tons / (WHEAT_AREA_1000_ha + 0.001)), 2) as Wheat_Yield_Ratio,
           ROUND((MAIZE_PRODUCTION_1000_tons / (MAIZE_AREA_1000_ha + 0.001)), 2) as Maize_Yield_Ratio
    FROM crop_data
    WHERE RICE_AREA_1000_ha > 0 AND WHEAT_AREA_1000_ha > 0 AND MAIZE_AREA_1000_ha > 0
    LIMIT 5;
"""

df4 = pd.read_sql(query_4, conn)
print(df4)

# -------------------------------------------------------------
# QUESTION 5: Yearly Production Growth of Cotton in Top 5 States
# -------------------------------------------------------------
print("\n📊 --- Query 5: Cotton Production Trends in Top States ---")

query_5 = """
    SELECT State_Name, Year, SUM(COTTON_PRODUCTION_1000_tons) as Total_Cotton
    FROM crop_data
    WHERE State_Name IN (
        SELECT State_Name 
        FROM crop_data 
        GROUP BY State_Name 
        ORDER BY SUM(COTTON_PRODUCTION_1000_tons) DESC 
        LIMIT 5
    )
    GROUP BY State_Name, Year
    ORDER BY State_Name, Year DESC
    LIMIT 10;
"""

df5 = pd.read_sql(query_5, conn)
print(df5)

# -------------------------------------------------------------
# QUESTION 6: Districts with the Highest Groundnut Production in 2017
# -------------------------------------------------------------
print("\n📊 --- Query 6: Highest Groundnut Production in 2017 ---")

query_6 = """
    SELECT Dist_Name, State_Name, GROUNDNUT_PRODUCTION_1000_tons
    FROM crop_data
    WHERE Year = 2017
    ORDER BY GROUNDNUT_PRODUCTION_1000_tons DESC
    LIMIT 5;
"""

df6 = pd.read_sql(query_6, conn)
print(df6)

# -------------------------------------------------------------
# QUESTION 7: Annual Average Maize Yield Across All States
# -------------------------------------------------------------
print("\n📊 --- Query 7: Average Maize Yield Across States ---")

query_7 = """
    SELECT State_Name, 
           ROUND(AVG(MAIZE_YIELD_Kg_per_ha), 2) as Avg_Maize_Yield
    FROM crop_data
    WHERE MAIZE_YIELD_Kg_per_ha > 0
    GROUP BY State_Name
    ORDER BY Avg_Maize_Yield DESC;
"""

df7 = pd.read_sql(query_7, conn)
print(df7)

# -------------------------------------------------------------
# QUESTION 8: Total Area Cultivated for Oilseeds in Each State
# -------------------------------------------------------------
print("\n📊 --- Query 8: Total Oilseeds Area Cultivated per State ---")

query_8 = """
    SELECT State_Name, 
           ROUND(SUM(OILSEEDS_AREA_1000_ha), 2) as Total_Oilseeds_Area
    FROM crop_data
    GROUP BY State_Name
    ORDER BY Total_Oilseeds_Area DESC;
"""

df8 = pd.read_sql(query_8, conn)
print(df8)

# -------------------------------------------------------------
# QUESTION 9: Districts with the Highest Rice Yield Records
# -------------------------------------------------------------
print("\n📊 --- Query 9: Districts with Highest Rice Yield Records ---")

query_9 = """
    SELECT Dist_Name, State_Name, 
           MAX(RICE_YIELD_Kg_per_ha) as Peak_Rice_Yield
    FROM crop_data
    GROUP BY Dist_Name, State_Name
    ORDER BY Peak_Rice_Yield DESC
    LIMIT 5;
"""

df9 = pd.read_sql(query_9, conn)
print(df9)

# -------------------------------------------------------------
# QUESTION 10: Rice vs Wheat Production Comparison (Last 10 Years)
# -------------------------------------------------------------
print("\n📊 --- Query 10: Rice vs Wheat Production (Top 5 States) ---")

query_10 = """
    SELECT State_Name, 
           ROUND(SUM(RICE_PRODUCTION_1000_tons), 2) as Total_Rice_Prod, 
           ROUND(SUM(WHEAT_PRODUCTION_1000_tons), 2) as Total_Wheat_Prod
    FROM crop_data
    WHERE Year >= (SELECT MAX(Year) - 10 FROM crop_data)
    GROUP BY State_Name
    ORDER BY (SUM(RICE_PRODUCTION_1000_tons) + SUM(WHEAT_PRODUCTION_1000_tons)) DESC
    LIMIT 5;
"""

df10 = pd.read_sql(query_10, conn)
print(df10)

# Safely close the connection at the end
conn.close()
  