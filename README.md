# SMT_Machine_Test

# 📘 Programming Tasks – Combined Submission
This repository contains **three small practical tasks** implemented using **SQL, Python, and JavaScript**.
## 🗄️ Task 1: SQL – Employee Table Management
### 📌 Description
This task demonstrates basic SQL operations including:

* Creating a table
* Inserting records
* Updating data

### 🧱 Table Structure
**employees**

* `id` (INT, Primary Key)
* `name` (VARCHAR)
* `department` (VARCHAR)
* `salary` (INT)
* `joining_date` (DATE)

### ✅ Operations Performed

* Table creation using `CREATE TABLE`
* Insertion of multiple sample records
* Updating employee salary using `UPDATE` with `WHERE` condition

### 💡 Concepts Covered

* DDL (Data Definition Language)
* DML (Data Manipulation Language)
* Primary Key usage

---

## 🧑‍🎓 Task 2: Python – Student Record Manager
### 📌 Description
A **console-based Python application** to manage student records using a **list of dictionaries**.

### ⚙️ Features

* Add a student (name, age, marks)
* View all students
* Search student by name
* Update student marks
* Delete a student
* Save data to JSON file on exit
* Load data from JSON file on program start

### 🧠 Approach

* Student data is stored in memory during runtime
* On exit, data is saved to `students.json`
* On next run, data is loaded back into memory

### 💡 Concepts Covered

* Lists and Dictionaries
* Functions
* File Handling (JSON)
* Basic data persistence

---

## 📝 Task 3: JavaScript – To-Do List Application
### 📌 Description
A browser-based To-Do List application built using HTML + JavaScript.

### ⚙️ Features

* Add new task
* View all tasks
* Mark task as completed (strike-through effect)
* Delete a task
* Store tasks in an array

### 🧠 Approach

* Tasks are stored as objects in an array
* Each task contains:
  * `text`
  * `completed` (boolean)
* UI is updated dynamically using DOM manipulation
* CSS class is applied to completed tasks for strike-through

### 💡 Concepts Covered

* Arrays & Objects
* Functions
* DOM Manipulation
* Event Handling
* Separation of logic (JS) and styling (CSS)

## Steps To Run ##
1) Open Sql file in the MySql Workbench or Sql Server Studio. Select the Commands and click on Run Button or Execute Button
2) Open The Python file in Any IDE such as Visual Studio Code. Click on New Terminal Button and Run the Script.
3) Open the html file by clicking on it , it will be opeaned in a browser.
**End of README**
