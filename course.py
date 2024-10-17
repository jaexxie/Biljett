from person import Person
from student import Student
from instructor import Instructor

class Course:
    
    def __init__(self) -> None:
        self.person = []
        self.students = []
        self.instructors = []
        self.courses = []

    def add_students(self) -> None:
        while True:
            name = input("Enter the student's name: ")
            if name.replace(' ', '').isalpha:
                name = name.capitalize().strip()
                break
            else:
                print("Invalid input, please enter a valid name. Only letter and spaces are allowed.")

        while True:
            email = input("Enter the student's email: ")
            if "@" in email and "." in email:
                email = email.strip()
                break
            else:
                print("Invalid email format. Please enter a valid email.")

        while True:
            try:
                id_number = int(input("Enter the student's ID number: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid numeric ID number.")

        while True:
            major = input("Enter the student's major: ")
            if major.replace(' ','').isalpha():
                major = major.strip().title()
                break
            else:
                print("Invalid input, please enter a valid major. Only letters and spaces are allowed.")

        while True:
            course_name = input("Enter course name: ")
            if course_name.replace(' ','').isalpha():
                course_name = course_name.strip().title()
                break
            else:
                print("Invalid input, please try again. Only letters and spaces are allowed.")

        while True:
            course_code = input("Enter course code: ")
            if course_code.isalnum():
                course_code = course_code.upper().strip()
                break
            else:
                print("Invalid input, please enter a valid alphanumeric course code.")


        student = Student(name, email, id_number, major, course_name, course_code)

        self.students.append(student)
        print(f"Student {name} has been added to the course {course_name}.")

    def add_instructors(self) -> None:

        while True:
            name = input("Enter the instructors name: ")
            if name.replace(' ', '').isalpha:
                name = name.capitalize().strip()
                break
            else:
                print("Invalid input, please enter a valid name. Only letters and spaces are allowed.")

        while True:
            email = input("Enter the instructor's email: ")
            if "@" in email and "." in email:
                email = email.strip()
                break
            else:
                print("Invalid email format. Please enter a valid email.")

        while True:
            try:
                id_number = int(input("Enter the instructor's ID number: "))
                break
            except ValueError:
                print("Invalid input, please enter a valid numeric ID number.")

        while True:
            department = input("Enter the instructor's department: ")
            if department.replace(' ','').isalpha():
                department = department.strip().title()
                break
            else:
                print("Invalid input, please enter a valid department. Only letters and spaces are allowed.")

        while True:
            course_name = input("Enter course name: ")
            if course_name.replace(' ','').isalpha():
                course_name = course_name.strip().title()
                break
            else:
                print("Invalid input, please try again. Only letters and spaces are allowed.")

        while True:
            course_code = input("Enter course code: ")
            if course_code.isalnum():
                course_code = course_code.upper().strip()
                break
            else:
                print("Invalid input, please enter a valid alphanumeric course code.")

        instructor = Instructor(name, email, id_number, department, course_name, course_code)

        self.instructors.append(instructor)
        print(f"Instructor {name} has been added to the course {course_name}.")

    def delete_student(self) -> None:
        if not self.students:
            print("No students to delete.")
            return

        delete_name = input("Enter the name of the student you would like to delete: ")

        for student in self.students:
            if student.name.lower() == delete_name.lower():
                self.students.remove(student)
                print(f"Student {student.name} has been removed.")
                return
            
        print(f"No student found with the name '{delete_name}'.")

    def delete_instructor(self) -> None:
        if not self.instructors:
            print("No instructors to delete.")
            return

        delete_name = input("Enter the name of the instructor you would like to delete: ")

        for instructor in self.instructors:
            if instructor.name.lower() == delete_name.lower():
                self.instructors.remove(instructor)
                print(f"Instructor {instructor.name} has been removed.")
                return
            
        print(f"No instructor found with the name '{delete_name}'.")

    def list_instructors(self) -> None:
        if not self.instructors:
            print("No instructors have been assigned yet")
        for instructor in self.instructors:
            print(f"Instructor Name: {instructor.name}, ID: {instructor.get_id()} Email: {instructor.email}, Department: {instructor.get_department()}, Course Name: {instructor.course_name}, Course Code: {instructor.course_code}")

    def list_students(self) -> None:
        if not self.students:
            print("No students have been accepted yet.")
        else:
            for student in self.students:
                print(f"Student Name: {student.name}, ID: {student.get_id()}, Email: {student.email}, Major: {student.get_major()}, Course Name: {student.course_name}, Course Code: {student.course_code}")