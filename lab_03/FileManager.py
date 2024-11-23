import csv
from Student import Student

class FileManager:
    @staticmethod
    def load_from_csv(filename, student_list):
       
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_list.add_student(Student(
                        name=row["name"], 
                        phone=row["phone"], 
                        age=int(row["age"]), 
                        email=row["email"]
                    ))
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

    @staticmethod
    def save_to_csv(filename, student_list):
       
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["name", "phone", "age", "email"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.students:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "age": student.age,
                        "email": student.email
                    })
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")
