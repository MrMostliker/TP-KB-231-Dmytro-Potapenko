import sys
from Student import Student
from StudentList import StudentList
from FileManager import FileManager

if __name__ == "__main__":
    student_list = StudentList()

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        FileManager.load_from_csv(input_file, student_list)
        
    while True:
        choice = input("Choose action [C - Create, U - Update, D - Delete, P - Print, X - Exit]: ")
        match choice.lower():
            case "c":
                name = input("Enter student's name: ")
                phone = input("Enter student's phone: ")
                age = int(input("Enter student's age: "))
                email = input("Enter student's email: ")
                student_list.add_student(Student(name, phone, age, email))
                print("New student has been added.")
            case "u":
                name = input("Enter the name of the student to update: ")
                phone = input("Enter new phone (or press Enter to skip): ")
                age = input("Enter new age (or press Enter to skip): ")
                email = input("Enter new email (or press Enter to skip): ")
                student_list.update_student(name, phone or None, int(age) if age else None, email or None)
                print("Student data updated.")
            case "d":
                name = input("Enter the name of the student to delete: ")
                student_list.delete_student(name)
                print(f"Student {name} has been deleted.")
            case "p":
                student_list.print_all()
            case "x":
                output_file = input_file if input_file else "students.csv"
                FileManager.save_to_csv(output_file, student_list)
                print(f"Data saved to {output_file}. Exiting...")
                break

            case _:
                print("Invalid choice, try again.")
