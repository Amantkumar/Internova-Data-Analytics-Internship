import pandas as pd
print("Series:"); print(pd.Series([85,90,78,92,88],name="Marks"))
df=pd.DataFrame({"Student_ID":[101,102,103,104,105],"Name":["Aarav","Diya","Rohan","Anaya","Vivaan"],
"Department":["Computer","IT","Computer","IT","Data Science"],"Marks":[85,92,78,88,95]})
print("\nDataFrame:\n",df); print("\nColumns:",df.columns.tolist()); print("Index:",df.index)
df["Result"]="Pass"; print("\nUpdated:\n",df)
