-- Task 4: INNER, LEFT and RIGHT JOIN
USE week3_analytics;
CREATE TABLE IF NOT EXISTS Departments(Department VARCHAR(50) PRIMARY KEY,HOD VARCHAR(50),Location VARCHAR(50));
SELECT s.Student_ID,s.Name,s.Department,d.HOD,d.Location FROM Students s INNER JOIN Departments d ON s.Department=d.Department;
SELECT s.Student_ID,s.Name,s.Department,d.HOD,d.Location FROM Students s LEFT JOIN Departments d ON s.Department=d.Department;
SELECT s.Student_ID,s.Name,d.Department,d.HOD,d.Location FROM Students s RIGHT JOIN Departments d ON s.Department=d.Department;