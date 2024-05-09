WITH employee_department AS
(
    SELECT 
    d.id, 
    d.name AS Department,
    e.salary AS Salary,
    e.name AS Employee,
    DENSE_RANK() OVER(PARTITION BY d.id ORDER BY e.salary DESC) as d_rank
    FROM Department d
    JOIN Employee e
    ON d.id = e.departmentId
)

SELECT Department, Employee, Salary
FROM employee_department
WHERE d_rank <=3