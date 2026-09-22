import pandas as pd
df=pd.read_csv("datasets/students.csv")
print("HEAD:\n",df.head()); print("\nTAIL:\n",df.tail()); print("\nShape:",df.shape);
print("\nColumns:",df.columns.tolist()); print("\nDtypes:\n",df.dtypes); 
print("\nINFO:"); df.info();
print("\nDESCRIBE:\n",df.describe())
