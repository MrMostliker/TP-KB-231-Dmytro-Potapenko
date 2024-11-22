# Start list
students = [
    {"name": "Bob", "phone": "0631234567", "age": 20, "email": "bob@example.com"},
    {"name": "Emma", "phone": "0631234567", "age": 22, "email": "emma@example.com"},
    {"name": "Jon", "phone": "0631234567", "age": 19, "email": "jon@example.com"},
    {"name": "Zak", "phone": "0631234567", "age": 21, "email": "zak@example.com"}
]

# List output
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

    # Insert position
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New student has been added.")
    return

# Deleting student
def deleteElement():
    name = input("Enter the name of the student to delete: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Student not found.")
    else:
        del students[deletePosition]
        print(f"Student {name} has been deleted.")
    return

# Updating student data
def updateElement():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student["name"] == name:
            print(f"Current data: {student}")
            student["phone"] = input("Enter new phone (or press Enter to skip): ") or student["phone"]
            student["age"] = int(input("Enter new age (or press Enter to skip): ") or student["age"])
            student["email"] = input("Enter new email (or press Enter to skip): ") or student["email"]
            print(f"Updated data: {student}")
            # Sorting after changes
            students.sort(key=lambda x: x["name"])
            return
    print("Student not found.")
    return

# Main display
def main():
    while True:
        choice = input("Choose action [C - Create, U - Update, D - Delete, P - Print, X - Exit]: ")
        match choice.lower():
            case "c":
                print("Adding a new student:")
                addNewElement()
                printAllList()
            case "u":
                print("Updating a student:")
                updateElement()
                printAllList()
            case "d":
                print("Deleting a student:")
                deleteElement()
                printAllList()
            case "p":
                print("Printing all students:")
                printAllList()
            case "x":
                print("Exiting...")
                break
            case _:
                print("Invalid choice, try again.")

# Start
main()
