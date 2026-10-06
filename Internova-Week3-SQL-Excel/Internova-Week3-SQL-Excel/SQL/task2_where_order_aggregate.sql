-- Task 2: WHERE, ORDER BY & Aggregates
SELECT * FROM Students WHERE Marks >= 80;
SELECT * FROM Students WHERE Age > 21;
SELECT Name, Marks FROM Students ORDER BY Marks DESC;
SELECT COUNT(*) AS Total_Students FROM Students;
SELECT SUM(Marks) AS Total_Marks FROM Students;
SELECT AVG(Marks) AS Average_Marks FROM Students;
SELECT MIN(Marks) AS Minimum_Marks FROM Students;
SELECT MAX(Marks) AS Maximum_Marks FROM Students;
