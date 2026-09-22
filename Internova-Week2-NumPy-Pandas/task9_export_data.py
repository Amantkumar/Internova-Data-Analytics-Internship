import pandas as pd
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent

# Dataset path
input_file = BASE_DIR / "datasets" / "students.csv"

# Output folder automatically create karega
output_folder = BASE_DIR / "output"
output_folder.mkdir(exist_ok=True)

# Read dataset
df = pd.read_csv(input_file)

# Add Average Marks
df["Average_Marks"] = df[["Maths", "Python", "Database"]].mean(axis=1)

# Add Performance
df["Performance"] = df["Average_Marks"].apply(
    lambda x: "Excellent"
    if x >= 90
    else ("Good" if x >= 80 else "Needs Improvement")
)

# Export
output_file = output_folder / "processed_students.csv"
df.to_csv(output_file, index=False)

print("Processed DataFrame:")
print(df.head())

print("\nExported successfully to:")
print(output_file)

# Verify exported file
verified_df = pd.read_csv(output_file)

print("\nVerified exported file:")
print(verified_df.head())