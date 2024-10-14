from student import Student
from instructor import Instructor

class Course:
    def __init__(self, course_name: str, course_code: str, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
        self.isntructors = []

    def add_student(self) -> str:
        name = input("Enter the student's name: ")
        email = input("Enter the student's email: ")
        id = int(input("Enter the student's ID number: "))
        major = input("Enter student's major: ")

        student = Student(name, email, id, major) 
        
        self.students.append(student)

    def add_instructor(self) -> str:
        name = input("Enter the instructors's name: ")
        email = input("Enter the instructor's email: ")
        id = int(input("Enter the instructor's ID number: "))
        department = input("Enter the instructor's department: ")

        instructor = Instructor(name, email, id, department)

        self.instructors.append(instructor)

        print(f"{name} has been added!")

    def list_students():
        pass

course_1 = Course("Algorithms", "CS102")

course_1.add_instructor()
