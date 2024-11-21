# Class init
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name='{self.name}', age={self.age})"

# List of students
students = [
    Student("Anna", 20),
    Student("Bohdan", 22),
    Student("Kateryna", 19),
    Student("Dmytro", 21),
]

# Sorting by age
sorted_students = sorted(students, key=lambda student: student.age)

# Output
for student in sorted_students:
    print(student)
