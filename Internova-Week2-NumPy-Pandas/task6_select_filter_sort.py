import pandas as pd
df=pd.read_csv("datasets/students.csv")
print("Selected columns:\n",df[["Name","Department","Maths","Python"]].head())
print("\nSelected rows:\n",df.iloc[:5])
print("\nPython >= 90:\n",df[df.Python>=90][["Name","Python"]])
print("\nMaths >=85 AND Attendance >=90:\n",df[(df.Maths>=85)&(df.Attendance>=90)][["Name","Maths","Attendance"]])
print("\nAscending:\n",df.sort_values("Python")[["Name","Python"]].head(10))
print("\nDescending:\n",df.sort_values("Python",ascending=False)[["Name","Python"]].head(10))
