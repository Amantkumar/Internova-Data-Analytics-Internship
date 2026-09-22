# Task 10: Mini Data Analysis Project
# Student Performance Analysis using Pandas and NumPy

import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATH
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

# Dataset path
input_file = BASE_DIR / "datasets" / "students.csv"

# Output folder
output_folder = BASE_DIR / "output"
output_folder.mkdir(exist_ok=True)

# --------------------------------------------------
# 2. LOAD DATASET
# --------------------------------------------------

df = pd.read_csv(input_file)

print("=" * 70)
print("       MINI DATA ANALYSIS PROJECT")
print("       STUDENT PERFORMANCE ANALYSIS")
print("=" * 70)

print("\n1. DATASET LOADED SUCCESSFULLY")
print("-" * 70)

print("Dataset Shape:", df.shape)

# --------------------------------------------------
# 3. DATA INSPECTION
# --------------------------------------------------

print("\n2. FIRST 5 RECORDS")
print("-" * 70)
print(df.head())

print("\n3. DATASET INFORMATION")
print("-" * 70)
print(df.info())

print("\n4. COLUMN NAMES")
print("-" * 70)
print(df.columns.tolist())

print("\n5. STATISTICAL SUMMARY")
print("-" * 70)
print(df.describe())

# --------------------------------------------------
# 4. CHECK MISSING VALUES
# --------------------------------------------------

print("\n6. MISSING VALUES")
print("-" * 70)

missing_values = df.isnull().sum()

print(missing_values)

total_missing = missing_values.sum()

print("\nTotal Missing Values:", total_missing)

# --------------------------------------------------
# 5. HANDLE MISSING VALUES
# --------------------------------------------------

print("\n7. HANDLING MISSING VALUES")
print("-" * 70)

numeric_columns = [
    "Age",
    "Maths",
    "Python",
    "Database",
    "Attendance"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

print("Missing numerical values handled successfully.")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 6. CREATE AVERAGE MARKS
# --------------------------------------------------

df["Average_Marks"] = df[
    ["Maths", "Python", "Database"]
].mean(axis=1)

print("\n8. AVERAGE MARKS CREATED")
print("-" * 70)

print(df[[
    "Name",
    "Maths",
    "Python",
    "Database",
    "Average_Marks"
]].head())

# --------------------------------------------------
# 7. FILTERING DATA
# --------------------------------------------------

print("\n9. FILTERING HIGH-PERFORMING STUDENTS")
print("-" * 70)

high_performers = df[
    df["Average_Marks"] >= 90
]

print(high_performers[[
    "Name",
    "Department",
    "Average_Marks"
]])

# --------------------------------------------------
# 8. SORTING DATA
# --------------------------------------------------

print("\n10. TOP 10 STUDENTS BY AVERAGE MARKS")
print("-" * 70)

top_students = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(10)

print(top_students[[
    "Name",
    "Department",
    "Average_Marks"
]])

# --------------------------------------------------
# 9. GROUPBY ANALYSIS
# --------------------------------------------------

print("\n11. DEPARTMENT-WISE GROUPBY ANALYSIS")
print("-" * 70)

department_analysis = df.groupby(
    "Department"
).agg(
    Average_Marks=("Average_Marks", "mean"),
    Average_Attendance=("Attendance", "mean"),
    Student_Count=("Student_ID", "count")
).round(2)

print(department_analysis)

# --------------------------------------------------
# 10. PIVOT TABLE
# --------------------------------------------------

print("\n12. PIVOT TABLE")
print("-" * 70)

pivot_table = pd.pivot_table(
    df,
    values="Average_Marks",
    index="Department",
    columns="Gender",
    aggfunc="mean"
).round(2)

print(pivot_table)

# --------------------------------------------------
# 11. KEY INSIGHTS
# --------------------------------------------------

print("\n13. KEY INSIGHTS")
print("=" * 70)

# Highest performing student
top_student = df.loc[
    df["Average_Marks"].idxmax()
]

# Highest average department
top_department = department_analysis[
    "Average_Marks"
].idxmax()

# Highest attendance department
best_attendance_department = department_analysis[
    "Average_Attendance"
].idxmax()

# Overall averages
overall_average_marks = df[
    "Average_Marks"
].mean()

overall_attendance = df[
    "Attendance"
].mean()

print(
    f"1. Highest-performing student: "
    f"{top_student['Name']} "
    f"({top_student['Average_Marks']:.2f} average marks)"
)

print(
    f"2. Department with highest average marks: "
    f"{top_department}"
)

print(
    f"3. Department with highest average attendance: "
    f"{best_attendance_department}"
)

print(
    f"4. Overall average marks: "
    f"{overall_average_marks:.2f}"
)

print(
    f"5. Overall average attendance: "
    f"{overall_attendance:.2f}%"
)

print(
    f"6. Number of high-performing students: "
    f"{len(high_performers)}"
)

# --------------------------------------------------
# 12. EXPORT CLEANED DATASET
# --------------------------------------------------

print("\n14. EXPORTING CLEANED DATA")
print("-" * 70)

output_file = output_folder / "student_performance_cleaned.csv"

df.to_csv(
    output_file,
    index=False
)

print("Cleaned dataset exported successfully.")
print("File Location:")
print(output_file)

# --------------------------------------------------
# 13. VERIFY EXPORTED DATA
# --------------------------------------------------

print("\n15. VERIFYING EXPORTED DATA")
print("-" * 70)

verified_data = pd.read_csv(output_file)

print("Exported dataset shape:", verified_data.shape)

print("\nFirst 5 rows of exported dataset:")
print(verified_data.head())

print("\n" + "=" * 70)
print("       MINI DATA ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)