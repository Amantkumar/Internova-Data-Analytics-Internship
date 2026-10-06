-- Task 4: SQL Joins
-- INNER JOIN: matching rows from both tables.
SELECT s.Student_ID,s.Name,d.Department,d.HOD
FROM Students_Department s INNER JOIN Departments d ON s.Department_ID=d.Department_ID;
-- LEFT JOIN: all left-table rows plus matches.
SELECT s.Student_ID,s.Name,d.Department,d.HOD
FROM Students_Department s LEFT JOIN Departments d ON s.Department_ID=d.Department_ID;
-- RIGHT JOIN: all right-table rows plus matches (supported by MySQL and other DBMS).
SELECT s.Student_ID,s.Name,d.Department,d.HOD
FROM Students_Department s RIGHT JOIN Departments d ON s.Department_ID=d.Department_ID;
