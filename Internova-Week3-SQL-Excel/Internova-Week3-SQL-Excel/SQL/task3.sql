-- Task 3: GROUP BY and HAVING
USE week3_analytics;
SELECT Department,COUNT(*) Student_Count,ROUND(AVG(Marks),2) Average_Marks,MAX(Marks) Highest_Marks FROM Students GROUP BY Department;
SELECT Department,ROUND(AVG(Marks),2) Average_Marks FROM Students GROUP BY Department HAVING AVG(Marks)>=80;