from student import Student
from instructor import Instructor

class Course:
    all_courses = []
    
    def __init__(self, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructors = []
        self.students = []
        self.courses = []

        
    def add_students(self):
        name = input("Enter the student's name: ")
        email = input("Enter the student's email: ")
        id_number = int(input("Enter the student's ID number: "))
        major = input("Enter the student's major: ")

        student = Student(name, email, id_number, major)

        self.students.append(student)
        print(f"Student {name} has been added to the course {self.course_name}.")

    def add_instructors(self):
        name = input("Enter the instructor's name: ")
        email = input("Enter the instructor's email: ")
        id_number = int(input("Enter the instructor's ID number: "))
        department = input("Enter the instructor's department: ")

        instructor = Instructor(name, email, id_number, department)

        self.instructors.append(instructor)
        print(f"Instructor {name} has been added to the course {self.course_name}.")

    def create_course(self) -> str:
        name = input("Enter course name: ")
        code = input("Enter course code: ")

        course = Course(name, code)

        self.courses.append(course)
        
        print(f"{name} has been added to the list of courses!")

    def list_instructors(self) -> str:
        for instructor in self.instructors:
            print(f"Name: {instructor.name}, Department: {instructor.department}, Email: {instructor.email}")

    def list_students(self) -> str:
        for student in self.students:
            print(f"Name: {student.name}, Department: {student.department}, Email: {student.email}")

    def list_courses(self) -> str:
        for course in self.courses:
            print(f"Course name: {course.course_name}, Course Code: {course.course_code}")