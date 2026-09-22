import pandas as pd
a=pd.read_csv("datasets/sales_part1.csv"); b=pd.read_csv("datasets/sales_part2.csv")
info=pd.DataFrame({"Product":["Laptop","Mouse","Keyboard","Monitor","Headphones"],"Category_Info":["Computer","Accessory","Accessory","Display","Audio"]})
print("MERGE:\n",a.merge(info,on="Product",how="left").head())
all_sales=pd.concat([a,b],ignore_index=True); print("\nCONCATENATE:\n",all_sales.head())
print("\nGROUPBY:\n",all_sales.groupby("Category")["Sales"].agg(["sum","mean","count","min","max"]))
print("\nPIVOT TABLE:\n",pd.pivot_table(all_sales,values="Sales",index="Region",columns="Category",aggfunc="sum",fill_value=0))
