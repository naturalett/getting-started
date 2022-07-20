# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.

class Student:
    def __init__(self) -> None:
        self.student_name = 'Terrance Morales'
        self.marks = 93

student = Student()
print(f"Student Name: {student.student_name}")
print(f"Student marks: {student.marks}")
student.student_name = "Angel Brooks"
student.marks = 95
print(f"Student Name: {student.student_name}")
print(f"Student marks: {student.marks}")
