-- Task 3: GROUP BY & HAVING
SELECT Department, COUNT(*) AS Student_Count, AVG(Marks) AS Average_Marks
FROM Students GROUP BY Department;
SELECT Department, AVG(Marks) AS Average_Marks
FROM Students GROUP BY Department HAVING AVG(Marks) >= 80;
