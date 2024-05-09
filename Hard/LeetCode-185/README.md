# Department Top Three Salaries

## Problem Statement
[Department Top Three Salaries Problem Description](https://leetcode.com/problems/department-top-three-salaries/description/)

## Explanation

### Algorithm:
1. Create a common table expression (CTE) named employee_department that joins the Department and Employee tables on the departmentId column, while also assigning a dense rank (d_rank) to each employee within their department based on salary.
2. Select the Department, Employee, and Salary columns from the employee_department CTE, filtering the results to only include rows where the d_rank is less than or equal to 3.