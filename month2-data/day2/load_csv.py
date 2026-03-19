# Month 2 - Day 2
# Loading and analyzing CSV data

import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv("students.csv")

# Step 2: Show full dataset
print("===== FULL DATASET =====")
print(df)

# Step 3: Show first 3 rows
print("\n===== FIRST 3 ROWS =====")
print(df.head(3))

# Step 4: Show information about the dataset
print("\n===== DATASET INFO =====")
print(df.info())

# Step 5: Show statistics
print("\n===== STATISTICS =====")
print(df.describe())

# Step 6: Calculate average
avg_math = df["Math"].mean()
print("\nAverage Math Score:", avg_math)

# Step 7: Find highest score
max_english = df["English"].max()
print("Highest English Score:", max_english)