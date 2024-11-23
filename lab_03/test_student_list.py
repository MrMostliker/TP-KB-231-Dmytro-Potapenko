import unittest
from Student import Student
from StudentList import StudentList

class TestStudentList(unittest.TestCase):
    def setUp(self):
    
        self.student_list = StudentList()
        self.student_list.add_student(Student("Alice", "123", 20, "alice@example.com"))
        self.student_list.add_student(Student("Bob", "456", 21, "bob@example.com"))
        self.student_list.add_student(Student("Charlie", "789", 22, "charlie@example.com"))

    def test_add_student(self):
       
        self.student_list.add_student(Student("David", "000", 23, "david@example.com"))
        self.assertEqual(len(self.student_list.students), 4)
        self.assertEqual(self.student_list.students[-1].name, "David")

    def test_delete_student(self):
       
        self.student_list.delete_student("Bob")
        self.assertEqual(len(self.student_list.students), 2)
        self.assertNotIn("Bob", [s.name for s in self.student_list.students])

    def test_delete_non_existent_student(self):
       
        self.student_list.delete_student("NonExistent")
        self.assertEqual(len(self.student_list.students), 3)  

    def test_update_student(self):
      
        self.student_list.update_student("Alice", phone="555", age=25, email="alice_new@example.com")
        student = next((s for s in self.student_list.students if s.name == "Alice"), None)
        self.assertIsNotNone(student)
        self.assertEqual(student.phone, "555")
        self.assertEqual(student.age, 25)
        self.assertEqual(student.email, "alice_new@example.com")

    def test_update_non_existent_student(self):
      
        self.student_list.update_student("NonExistent", phone="999")
        self.assertEqual(len(self.student_list.students), 3) 

    def test_print_all(self):
        
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        self.student_list.print_all()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Alice", output)
        self.assertIn("Bob", output)
        self.assertIn("Charlie", output)

if __name__ == "__main__":
    unittest.main()
