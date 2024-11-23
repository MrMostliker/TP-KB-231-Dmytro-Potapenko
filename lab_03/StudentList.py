from Student import Student

class StudentList:
    def __init__(self):
        
        self.students = []

    def add_student(self, student):
      
        self.students.append(student)
        self.students.sort(key=lambda s: s.name)

    def delete_student(self, name):
        
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name, phone=None, age=None, email=None):
      
        for student in self.students:
            if student.name == name:
                if phone:
                    student.phone = phone
                if age:
                    student.age = age
                if email:
                    student.email = email
                break

    def print_all(self):
       
        for student in self.students:
            print(student)
