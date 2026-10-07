-- Task 2: WHERE, ORDER BY and aggregates
USE week3_analytics;
SELECT * FROM Students WHERE Marks>=85;
SELECT Name,Department,Marks FROM Students ORDER BY Marks DESC;
SELECT COUNT(*) Total_Students,SUM(Marks) Total_Marks,ROUND(AVG(Marks),2) Average_Marks,MIN(Marks) Minimum_Marks,MAX(Marks) Maximum_Marks FROM Students;