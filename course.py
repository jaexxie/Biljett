from person import Person
from student import Student
from instructor import Instructor

class Course:
    
    def __init__(self):
        self.person = []
        self.students = []
        self.instructors = []
        self.courses = []

    def add_students(self):
        name = input("Enter the student's name: ")
        email = input("Enter the student's email: ")
        id_number = int(input("Enter the student's ID number: "))
        major = input("Enter the student's major: ")
        course_name = input("Enter course name: ")
        course_code = input("Enter course code: ")


        student = Student(name, email, id_number, major, course_name, course_code)

        self.students.append(student)
        print(f"Student {name} has been added to the course {course_name}.")

    def add_instructors(self):
        name = input("Enter the instructor's name: ")
        email = input("Enter the instructor's email: ")
        id_number = int(input("Enter the instructor's ID number: "))
        department = input("Enter the instructor's department: ")
        course_name = input("Enter course name: ")
        course_code = input("Enter course code: ")

        instructor = Instructor(name, email, id_number, department, course_name, course_code)

        self.instructors.append(instructor)
        print(f"Instructor {name} has been added to the course {course_name}.")

    def create_course(self) -> str:
        name = input("Enter course name: ")
        code = input("Enter course code: ")

        course = Course(name, code)

        self.courses.append(course)
        
        print(f"{name} has been added to the list of courses!")

    def list_instructors(self) -> str:
        if not self.instructors:
            print("No instructors have been assigned yet")
        for instructor in self.instructors:
            print(f"Name: {instructor.name}, Department: {instructor.department}, Email: {instructor.email}")

    def list_students(self) -> str:
        if not self.students:
            print("No students have been accepted yet.")
        else:
            for student in self.students:
                print(f"Student name: {student.name}, Email: {student.email}")

    def list_courses(self) -> str:
        if not self.courses:
            print("No courses have been created yet.")
        else:
            for course in self.courses:
                print(f"Course name: {course.course_name}, Course Code: {course.course_code}")

    def display_enrollment_details(self):
            #Course name, Instructor, All the students assigned to that course
            course_name = input("Enter the course: ")

            if course_name in self.courses:
                for course in Course.all_courses:
                    if course.course_name == course_name:
                        print(f"Course name: {course.course_name}")

                        print("Instructors: ")
                        if not course.instructors:
                            print("No instructors")
                        else:
                            for instructor in course.instructors:
                                print(f"Name: {instructor.name}, Email: {instructor.email}")

                        print("Students")
                        if not course.students:
                            print("No students")
                        else:
                            for student in course.students:
                                print(f"Name: {student.name}, Email: {student.email}")
                        break
            else:
                print("Course not found")        
