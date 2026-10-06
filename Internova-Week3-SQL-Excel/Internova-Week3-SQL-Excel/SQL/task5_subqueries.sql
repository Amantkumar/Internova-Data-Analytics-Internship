-- Task 5: Subqueries
-- Employees earning above average salary.
SELECT Employee_ID,Name,Salary FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
-- Products priced above average.
SELECT Product_ID,Product,Price FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
