-- Task 5: Subqueries
USE week3_analytics;
SELECT Employee_Name,Department,Salary FROM Employees WHERE Salary>(SELECT AVG(Salary) FROM Employees) ORDER BY Salary DESC;
SELECT Product,SUM(Total_Sales) Product_Sales FROM Sales GROUP BY Product
HAVING SUM(Total_Sales)>(SELECT AVG(Product_Total) FROM (SELECT Product,SUM(Total_Sales) Product_Total FROM Sales GROUP BY Product) ProductSummary)
ORDER BY Product_Sales DESC;