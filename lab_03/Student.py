class Student:
    def __init__(self, name, phone, age, email):
       
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email

    def __str__(self):
       
        return f"Name: {self.name}, Phone: {self.phone}, Age: {self.age}, Email: {self.email}"
