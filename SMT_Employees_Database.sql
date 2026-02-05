create database SMT_Employee;
use smt_employee;

/*Part A Create employees Table*/
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INT,
    joining_date DATE
);

/*Part B insert sample records*/
INSERT INTO employees (id, name, department, salary, joining_date) VALUES
(1, 'Amit Sharma', 'HR', 40000, '2021-03-15'),
(2, 'Neha Verma', 'IT', 60000, '2020-07-10'),
(3, 'Rahul Singh', 'Finance', 55000, '2019-11-25'),
(4, 'Priya Gupta', 'IT', 65000, '2022-01-05'),
(5, 'Ankit Jain', 'Marketing', 45000, '2021-09-18');

/*Part C*/
/*Task 1 select all employees*/
select * from employees;

/*Task 2 select all employees with salary greater than 30000*/
select * from employees where salary>30000;

/*Task 3 select all employees witd dept as IT*/
select * from employees where department="IT";

/*Task 4 Update Salary of Employee*/
update employees set salary=32000 where id=2;

/*Task 5 Delete employee*/
delete from employees where id=5;

/*Task 6 Highest Salary*/
select id,name from employees where salary =(select max(salary) from employees);

/*Task 7 Total employee count*/
select count(*) from employees;




