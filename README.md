# SMT_Machine_Test

# Programming Tasks – Combined Submission
This repository contains **three small practical tasks** implemented using **SQL, Python, and JavaScript**.
## Task 1: SQL – Employee Table Management
### Description
This task demonstrates basic SQL operations including:

* Creating a table
* Inserting records
* Updating data

### Table Structure
**employees**

* `id` (INT, Primary Key)
* `name` (VARCHAR)
* `department` (VARCHAR)
* `salary` (INT)
* `joining_date` (DATE)

### Operations Performed

* Table creation using `CREATE TABLE`
* Insertion of multiple sample records
* Updating employee salary using `UPDATE` with `WHERE` condition

### Concepts Covered

* DDL (Data Definition Language)
* DML (Data Manipulation Language)
* Primary Key usage

---

## Task 2: Python – Student Record Manager
###  Description
A **console-based Python application** to manage student records using a **list of dictionaries**.

### Features

* Add a student (name, age, marks)
* View all students
* Search student by name
* Update student marks
* Delete a student
* Save data to JSON file on exit
* Load data from JSON file on program start

### Approach

* Student data is stored in memory during runtime
* On exit, data is saved to `students.json`
* On next run, data is loaded back into memory

### Concepts Covered

* Lists and Dictionaries
* Functions
* File Handling (JSON)
* Basic data persistence

---

## Task 3: JavaScript – To-Do List Application
### Description
A browser-based To-Do List application built using HTML + JavaScript.

### Features

* Add new task
* View all tasks
* Mark task as completed (strike-through effect)
* Delete a task
* Store tasks in an array

### Approach

* Tasks are stored as objects in an array
* Each task contains:
  * `text`
  * `completed` (boolean)
* UI is updated dynamically using DOM manipulation
* CSS class is applied to completed tasks for strike-through

### Concepts Covered

* Arrays & Objects
* Functions
* DOM Manipulation
* Event Handling
* Separation of logic (JS) and styling (CSS)

## Steps To Run ##
Steps to Run The Sql File

1)Open your SQL database tool.

2)Create or select a database.

3)Copy the CREATE TABLE query and execute it.

4)Run the INSERT INTO query to add sample records.

5)Run the UPDATE query to modify employee salary.

6)Use SELECT * FROM employees; to verify the data.

## Steps For Python File ##
1)Save the Python program as Student_Management_python.py

2)Open terminal or command prompt.

3)Navigate to the project folder.

4)Run the program using: python Student_Management_python.py

5)Use the menu options to:

Add students

View records

Update or delete students

## HTML and JS Files ##

1)Ensure the following files are in the same folder:
a)ToDoList.html
b)ToDoList.js

2)Double-click index.html OR

3)Right-click → Open with browser.

4)Enter a task in the input box and click Add Task.

5)Use Complete to mark task as done.

6)Use Delete to remove a task.

<img width="1920" height="1008" alt="Student_Management_Python py - Visual Studio Code 05-02-2026 2 53 04 PM" src="https://github.com/user-attachments/assets/d07bc568-f15d-4032-ae7f-a5bf09f5aed9" />
<img width="1920" height="1008" alt="Student_Management_Python py - Visual Studio Code 05-02-2026 2 54 14 PM" src="https://github.com/user-attachments/assets/62097272-afd4-48d4-87d4-7ff9c33a3b29" />
<img width="1920" height="1008" alt="To-Do List - Google Chrome 05-02-2026 2 43 20 PM" src="https://github.com/user-attachments/assets/ca29bdb6-890d-43ae-93e2-2490a413e812" />


**End of README**
