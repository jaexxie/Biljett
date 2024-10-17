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

    def create_course(self) -> None:

        while True:
            name = input("Enter course name: ")
            if name.replace(' ', '').isalpha:
                name = name.capitalize().strip()
                break
            else:
                print("Invalid input, please enter a valid course name. Only letters and spaces are allowed.")

        while True:
            course_code = input("Enter course code: ")
            if course_code.isalnum():
                course_code = course_code.upper().strip()
                break
            else:
                print("Invalid input, please enter a valid alphanumeric course code.")

        course = Course(name, course_code)

        self.courses.append(course)
        
        print(f"{name} has been added to the list of courses!")

    def delete_student(self) -> None:
        if not self.students:
            print("No students to delete.")

            delete_name = input("Enter the name of the student you would like to delete: ")

            for student in self.students:
                if student.name.lower() == delete_name.lower():
                    self.students.remove(student)
                    print(f"Student {student.name} has been removed.")
                
            print(f"No student found with the name '{student.name}'.")

    def delete_instructor(self) -> None:
            if not self.instructors:
                print("No instructors to delete.")

                delete_name = input("Enter the name of the instructor you would like to delete: ")

                for instructor in self.instructors:
                    if instructor.name.lower() == delete_name.lower():
                        self.instructors.remove(instructor)
                        print(f"Student {instructor.name} has been removed.")
                    
                print(f"No student found with the name '{instructor.name}'.")

    def delete_course(self) -> None:
        if not self.courses:
            print("No courses to delete.")

            delete_course = input("Enter the course code of the course you would like to delete: ")

            for course in self.courses:
                if course.course_code.lower() == delete_course.lower():
                    self.courses.remove(course)
                    print(f"Course {course.course_code} has been deleted.")
                
            print(f"No course found with the code {course.course_code}.")

    def list_instructors(self) -> None:
        if not self.instructors:
            print("No instructors have been assigned yet")
        for instructor in self.instructors:
            print(f"Name: {instructor.name}, Department: {instructor.department}, Email: {instructor.email}")

    def list_students(self) -> None:
        if not self.students:
            print("No students have been accepted yet.")
        else:
            for student in self.students:
                print(f"Student name: {student.name}, Email: {student.email}")

    def list_courses(self) -> None:
        if not self.courses:
            print("No courses have been created yet.")
        else:
            for course in self.courses:
                print(f"Course name: {course.course_name}, Course Code: {course.course_code}")

    def display_enrollment_details(self) -> None:
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
