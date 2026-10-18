from pathlib import Path
import pandas as pd, numpy as np, matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parents[1]; DATA=BASE/"datasets"; OUT=BASE/"outputs"; FIG=BASE/"visualizations"
OUT.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
sales=pd.read_csv(DATA/"Sales_Raw.csv",parse_dates=["Date"]); customers=pd.read_csv(DATA/"Customers.csv"); products=pd.read_csv(DATA/"Products.csv")
print("Raw shape:",sales.shape); print("Missing values:\n",sales.isna().sum()); print("Duplicate Sale_IDs:",sales.Sale_ID.duplicated().sum())
sales=sales.drop_duplicates(subset="Sale_ID").copy()
# In this dataset Discount is stored as a percentage (e.g., 5 means 5%).
# Where a field is missing but Sales_Amount is present, infer the missing value algebraically.
q_missing=sales.Quantity.isna() & sales.Sales_Amount.notna() & sales.Unit_Price.notna() & sales.Discount.notna()
sales.loc[q_missing,"Quantity"]=(sales.loc[q_missing,"Sales_Amount"]/(sales.loc[q_missing,"Unit_Price"]*(1-sales.loc[q_missing,"Discount"]/100))).round()
d_missing=sales.Discount.isna() & sales.Sales_Amount.notna() & sales.Unit_Price.notna() & sales.Quantity.notna() & (sales.Unit_Price* sales.Quantity != 0)
sales.loc[d_missing,"Discount"]=(1-sales.loc[d_missing,"Sales_Amount"]/(sales.loc[d_missing,"Unit_Price"]*sales.loc[d_missing,"Quantity"]))*100
sales["Quantity"]=sales.Quantity.fillna(sales.Quantity.median()).astype(int); sales["Discount"]=sales.Discount.fillna(0)
sales["Sales_Amount"]=(sales.Quantity*sales.Unit_Price*(1-sales.Discount/100)).round(2); sales["Month"]=sales.Date.dt.strftime("%b"); sales["Month_Number"]=sales.Date.dt.month; sales["Year"]=sales.Date.dt.year
sales.to_csv(OUT/"Sales_Cleaned.csv",index=False)
df=sales.merge(customers,on="Customer_ID",how="left").merge(products[["Product_ID","Product","Category"]],on="Product_ID",how="left"); df.to_csv(OUT/"Sales_Analysis_Enriched.csv",index=False)
df.describe(include="all").transpose().to_csv(OUT/"descriptive_statistics.csv"); df.select_dtypes(include=np.number).corr().to_csv(OUT/"correlation_matrix.csv")
monthly=df.groupby(["Month_Number","Month"],as_index=False).Sales_Amount.sum().sort_values("Month_Number"); category=df.groupby("Category",as_index=False).Sales_Amount.sum().sort_values("Sales_Amount",ascending=False); region=df.groupby("Region",as_index=False).Sales_Amount.sum().sort_values("Sales_Amount",ascending=False); segment=df.groupby("Segment",as_index=False).Sales_Amount.sum().sort_values("Sales_Amount",ascending=False)
def chart(file,title,x,y,kind="bar",xlabel="",ylabel="Sales Amount (₹)"):
 plt.figure(figsize=(9,5)); (plt.plot(x,y,marker="o") if kind=="line" else plt.scatter(x,y,alpha=.7) if kind=="scatter" else plt.bar(x,y)); plt.title(title); plt.xlabel(xlabel or "Month / Category / Region"); plt.ylabel(ylabel); plt.xticks(rotation=20,ha="right"); plt.tight_layout(); plt.savefig(FIG/file,dpi=150); plt.close()
chart("01_monthly_sales_trend.png","Monthly Sales Trend",monthly.Month,monthly.Sales_Amount,"line","Month")
chart("02_sales_by_category.png","Total Sales by Category",category.Category,category.Sales_Amount,xlabel="Category")
chart("03_sales_by_region.png","Total Sales by Region",region.Region,region.Sales_Amount,xlabel="Region")
chart("04_sales_by_segment.png","Sales by Customer Segment",segment.Segment,segment.Sales_Amount,xlabel="Customer Segment")
chart("05_quantity_vs_sales.png","Quantity vs Sales Amount",df.Quantity,df.Sales_Amount,"scatter","Quantity","Sales Amount (₹)")
plt.figure(figsize=(9,5)); plt.hist(df.Sales_Amount,bins=18); plt.title("Distribution of Sales Amount"); plt.xlabel("Sales Amount (₹)"); plt.ylabel("Frequency"); plt.tight_layout(); plt.savefig(FIG/"06_sales_distribution.png",dpi=150); plt.close()
q1,q3=df.Sales_Amount.quantile([.25,.75]); iqr=q3-q1; df[(df.Sales_Amount<q1-1.5*iqr)|(df.Sales_Amount>q3+1.5*iqr)].to_csv(OUT/"sales_outliers_iqr.csv",index=False)
for n,d in [("Sales_by_Category",category),("Sales_by_Region",region),("Sales_by_Month",monthly),("Sales_by_Segment",segment)]: d.to_csv(OUT/(n+".csv"),index=False)
print("Cleaned records:",len(df)); print("Total sales:",round(df.Sales_Amount.sum(),2)); print("Average order value:",round(df.Sales_Amount.mean(),2)); print("Top category:",category.iloc[0].Category); print("Top region:",region.iloc[0].Region)
