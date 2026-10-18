# Suggested DAX Measures

```DAX
Total Sales = SUM(Sales_Clean[Sales_Amount])
Total Records = COUNTROWS(Sales_Clean)
Average Order Value = DIVIDE([Total Sales], [Total Records])
Total Quantity = SUM(Sales_Clean[Quantity])
Maximum Sale = MAX(Sales_Clean[Sales_Amount])
Minimum Sale = MIN(Sales_Clean[Sales_Amount])
```
