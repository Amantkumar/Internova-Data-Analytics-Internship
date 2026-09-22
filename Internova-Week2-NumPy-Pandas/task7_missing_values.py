import pandas as pd
df=pd.read_csv("datasets/missing_students.csv")
print("BEFORE:\n",df); print("\nMissing counts:\n",df.isna().sum())
print("\nAfter dropna:\n",df.dropna())
filled=df.copy()
for c in ["Age","Maths","Python","Database","Attendance"]: filled[c]=filled[c].fillna(filled[c].mean())
print("\nAfter filling numeric missing values with mean:\n",filled)
print("\nImportance: Missing data can reduce data quality and affect analytical results.")
