# Write your MySQL query statement below
select emp.unique_id, employees.name from employees 
left join employeeuni as emp 
on employees.id = emp.id;