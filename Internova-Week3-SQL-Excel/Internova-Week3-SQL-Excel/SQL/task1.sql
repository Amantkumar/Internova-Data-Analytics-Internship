-- Task 1: SELECT
CREATE DATABASE IF NOT EXISTS week3_analytics;
USE week3_analytics;
CREATE TABLE IF NOT EXISTS Students(Student_ID INT PRIMARY KEY,Name VARCHAR(50),Department VARCHAR(50),Age INT,Marks DECIMAL(5,2));
SELECT * FROM Students;
SELECT Name,Department,Marks FROM Students;
SELECT Name AS Student_Name,Marks AS Final_Marks FROM Students;