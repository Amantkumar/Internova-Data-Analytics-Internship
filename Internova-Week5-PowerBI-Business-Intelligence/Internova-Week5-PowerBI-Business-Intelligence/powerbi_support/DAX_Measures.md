# DAX Measures

```DAX
Total Sales = SUM(Sales_Clean[Sales_Amount])
Average Sales = AVERAGE(Sales_Clean[Sales_Amount])
Total Records = COUNTROWS(Sales_Clean)
Maximum Sale = MAX(Sales_Clean[Sales_Amount])
Minimum Sale = MIN(Sales_Clean[Sales_Amount])
Total Quantity = SUM(Sales_Clean[Quantity])
Average Order Value = DIVIDE([Total Sales], [Total Records])
Sales % of Total = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Sales_Clean)))
```

Use Total Sales, Total Records and Average Order Value as the 3 main KPI cards.
