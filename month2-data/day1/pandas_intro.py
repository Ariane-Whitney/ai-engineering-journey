# Day 7 - Introduction to Pandas
# Concepts: DataFrame, Basic Analysis

import pandas as pd

# Create sample student data
data = {
    "Name": ["Alice", "Bob", "Whitney", "David"],
    "Math": [85, 78, 92, 88],
    "Science": [90, 74, 95, 80],
    "English": [88, 82, 91, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nBasic Statistics:")
print(df.describe())

print("\nAverage Math Score:")
print(df["Math"].mean())

print("\nHighest Science Score:")
print(df["Science"].max())