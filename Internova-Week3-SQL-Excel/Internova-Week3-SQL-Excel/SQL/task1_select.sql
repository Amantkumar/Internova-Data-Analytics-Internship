-- Task 1: SELECT
CREATE TABLE Students (Student_ID INTEGER, Name TEXT, Department TEXT, Age INTEGER, Marks REAL);
SELECT * FROM Students;
SELECT Name, Department, Marks FROM Students;
SELECT Name AS Student_Name, Marks AS Final_Marks FROM Students;
