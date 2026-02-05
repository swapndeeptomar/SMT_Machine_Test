import json
import os
students = []

def load_students():
    global students
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            students = json.load(file)

def add_student():
    name = input("Student name: ").strip()
    age = int(input("Age: "))
    marks = int(input("Marks: "))

    students.append({
        "name": name,
        "age": age,
        "marks": marks
    })

    print(f"Student {name} added successfully \n")


def view_students():
    if len(students) == 0:
        print("No Student Found.\n")
        return

    print("\nStudent List:")
    for student in students:
        print(f"- {student['name']} | Age: {student['age']} | Marks: {student['marks']}")
    print()


def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def search_student():
    name = input("Search student name: ")
    student = find_student(name)

    if student:
        print(f"Found → {student}\n")
    else:
        print("Student nahi mila.\n")


def update_marks():
    name = input("Student name to update marks: ")
    student = find_student(name)

    if student:
        student["marks"] = int(input("New marks: "))
        print("Marks updated \n")
    else:
        print("No Student Found.\n")


def delete_student():
    name = input("Student name to delete: ")
    student = find_student(name)

    if student:
        students.remove(student)
        print("Student deleted \n")
    else:
        print("Student Found.\n")

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

load_students()
while True:
    print("===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        save_students()
        print("Thanks For Using System")
        break
    else:
        print("Wrong Choice Try Again Later.\n")
