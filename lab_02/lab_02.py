import csv
import sys
import unittest

# Global list
students = []

# CSV data upload
def loadFromCSV(filename):
    global students
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = sorted(
                [
                    {"name": row["name"], "phone": row["phone"], "age": int(row["age"]), "email": row["email"]}
                    for row in reader
                ],
                key=lambda x: x["name"]
            )
            print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")

# CSV data save
def saveToCSV(filename):
    global students
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
            print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

# List print
def printAllList():
    for elem in students:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Age: {elem['age']}, Email: {elem['email']}")
    return

# Adding a student
def addNewElement():
    name = input("Enter student's name: ")
    phone = input("Enter student's phone: ")
    age = int(input("Enter student's age: "))
    email = input("Enter student's email: ")
    newItem = {"name": name, "phone": phone, "age": age, "email": email}
    students.append(newItem)
    students.sort(key=lambda x: x["name"])
    print("New student has been added.")

# Deleting a student
def deleteElement():
    name = input("Enter the name of the student to delete: ")
    global students
    students = [student for student in students if student["name"] != name]
    print(f"Student {name} has been deleted.")

# Student data update
def updateElement():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student["name"] == name:
            print(f"Current data: {student}")
            student["phone"] = input("Enter new phone (or press Enter to skip): ") or student["phone"]
            student["age"] = int(input("Enter new age (or press Enter to skip): ") or student["age"])
            student["email"] = input("Enter new email (or press Enter to skip): ") or student["email"]
            students.sort(key=lambda x: x["name"])
            print("Student data updated.")
            return
    print("Student not found.")

# Main display
def main():
    if len(sys.argv) > 1:
        loadFromCSV(sys.argv[1])
    else:
        print("No input CSV file specified.")

    while True:
        choice = input("Choose action [C - Create, U - Update, D - Delete, P - Print, X - Exit]: ")
        match choice.lower():
            case "c":
                addNewElement()
            case "u":
                updateElement()
            case "d":
                deleteElement()
            case "p":
                printAllList()
            case "x":
                saveToCSV("D:\Desktop\Cвои лабы\Второй курс\Технології програмування\Repos\TP-KB-231-Dmytro-Potapenko\lab_02\lab2.csv")
                print("Exiting...")
                break
            case _:
                print("Invalid choice, try again.")

# Unit-tests
class TestStudentDirectory(unittest.TestCase):
    def setUp(self):
        global students
        students = [
            {"name": "Alice", "phone": "123", "age": 20, "email": "alice@example.com"},
            {"name": "Bob", "phone": "456", "age": 21, "email": "bob@example.com"}
        ]

    def test_addNewElement(self):
        global students
        original_length = len(students)
        students.append({"name": "Charlie", "phone": "789", "age": 22, "email": "charlie@example.com"})
        students.sort(key=lambda x: x["name"])
        self.assertEqual(len(students), original_length + 1)
        self.assertEqual(students[-1]["name"], "Charlie")

    def test_deleteElement(self):
        global students
        original_length = len(students)
        students = [student for student in students if student["name"] != "Alice"]
        self.assertEqual(len(students), original_length - 1)
        self.assertNotIn({"name": "Alice", "phone": "123", "age": 20, "email": "alice@example.com"}, students)

    def test_updateElement(self):
        for student in students:
            if student["name"] == "Bob":
                student["phone"] = "999"
                break
        self.assertEqual(students[1]["phone"], "999")

if __name__ == "__main__":
    main()
