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
            name = input("Enter the student's name: ").strip()
            if name.replace(' ', '').isalpha():
                name = name.capitalize()
                break
            else:
                print("Invalid input, please enter a valid name. Only letter and spaces are allowed.")

        while True:
            email = input("Enter the student's email: ").strip()
            if "@" in email and "." in email:
                email = email
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
            major = input("Enter the student's major: ").strip()
            if major.replace(' ','').isalpha():
                major = major.title()
                break
            else:
                print("Invalid input, please enter a valid major. Only letters and spaces are allowed.")

        while True:
            course_name = input("Enter course name: ").strip()
            if course_name.replace(' ','').isalpha():
                course_name = course_name.title()
                break
            else:
                print("Invalid input, please try again. Only letters and spaces are allowed.")

        while True:
            course_code = input("Enter course code: ").strip()
            if course_code.isalnum():
                course_code = course_code.upper()
                break
            else:
                print("Invalid input, please enter a valid alphanumeric course code.")

        student = Student(name, email, id_number, major, course_name, course_code)

        self.students.append(student)
        print(f"Student {name} has been added to the course {course_name}.")

    def add_instructors(self) -> None:
        while True:
            name = input("Enter the instructors name: ").strip()
            if name.replace(' ', '').isalpha():
                name = name.capitalize()
                break
            else:
                print("Invalid input, please enter a valid name. Only letters and spaces are allowed.")

        while True:
            email = input("Enter the instructor's email: ").strip()
            if "@" in email and "." in email:
                email = email
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
            department = input("Enter the instructor's department: ").strip()
            if department.replace(' ','').isalpha():
                department = department.title()
                break
            else:
                print("Invalid input, please enter a valid department. Only letters and spaces are allowed.")

        while True:
            course_name = input("Enter course name: ").strip()
            if course_name.replace(' ','').isalpha():
                course_name = course_name.title()
                break
            else:
                print("Invalid input, please try again. Only letters and spaces are allowed.")

        while True:
            course_code = input("Enter course code: ").strip()
            if course_code.isalnum():
                course_code = course_code.upper()
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

    def update_student(self) -> None:
        while True:
            update_student = input("Enter the name of the student you would like to update: ")

            for student in self.students:
                if student.name.lower() == update_student.lower():
                    print(f"Updating student: {student}")

                    while True:
                        new_name = input("Enter new name: ").strip()
                        if new_name.isalpha():
                            student.name = new_name.capitalize()
                            break
                        else:
                            print("Invalid input, please enter a valid name.")

                    while True:
                        new_email = input("Enter new email: ").strip()
                        if "@" in new_email and "." in new_email:
                            student.email = new_email
                            break
                        else:
                            print("Invalid input, please enter a valid email.")

                    while True:
                        try:
                            new_id = int(input("Enter new ID: ").strip())
                            student._Person__id_number = new_id
                            break
                        except ValueError:
                            print("Invalid input, pleaser a valid ID number.")

                    while True:
                        new_major = input("Enter new major: ").strip()
                        if new_major.replace(' ','').isalpha():
                            student._Student__major = new_major.title()
                            break
                        else:
                            print("Invalid input, please enter a valid major.")

                    while True:
                        new_course_name = input("Enter new course name: ").strip()
                        if new_course_name.replace(' ', '').isalpha():
                            student.course_name = new_course_name.title()
                            break
                        else:
                            print("Invalid input, please enter a valid course name.")

                    while True:
                        new_course_code = input("Enter new course code: ").strip()
                        if new_course_code.isalnum():
                            student.course_code = new_course_code.upper()
                            break
                        else:
                            print("Invalid input, please enter a valid course code.")

                    print(f"Student has been updated successfully.")
                    return                        
        
            print(f"No student found with the name '{update_student}'")
            return

    def update_instructor(self) -> None:
        while True:
            update_instructor = input("Enter the name of the instructor you would like to update: ")

            for instructor in self.instructors:
                if instructor.name.lower() == update_instructor.lower():
                    print(f"Updating instructor: {instructor}")

                    while True:
                        new_name = input("Enter new name: ").strip()
                        if new_name.isalpha():
                            instructor.name = new_name.capitalize()
                            break
                        else:
                            print("Invalid input, please enter a valid name.")

                    while True:
                        new_email = input("Enter new email: ").strip()
                        if "@" in new_email and "." in new_email:
                            instructor.email = new_email
                            break
                        else:
                            print("Invalid input, please enter a valid email.")

                    while True:
                        try:
                            new_id = int(input("Enter new ID: ").strip())
                            instructor._Person__id_number = new_id
                            break
                        except ValueError:
                            print("Invalid input, pleaser a valid ID number.")

                    while True:
                        new_department = input("Enter new major: ").strip()
                        if new_department.replace(' ','').isalpha():
                            instructor._Instructor__department = new_department.title()
                            break
                        else:
                            print("Invalid input, please enter a valid major.")

                    while True:
                        new_course_name = input("Enter new course name: ").strip()
                        if new_course_name.replace(' ', '').isalpha():
                            instructor.course_name = new_course_name.title()
                            break
                        else:
                            print("Invalid input, please enter a valid course name.")

                    while True:
                        new_course_code = input("Enter new course code: ").strip()
                        if new_course_code.isalnum():
                            instructor.course_code = new_course_code.upper()
                            break
                        else:
                            print("Invalid input, please enter a valid course code.")

                    print(f"Instructor has been updated successfully.")
                    return                        
        
            print(f"No instructor found with the name '{update_instructor}'")
            return

    def search_student(self) -> None:
        search_name = input("Enter the name of the student you're searching for: ")
        for student in self.students:
            if student.name.lower() == search_name.lower():
                print(student)
                return student
        print(f"No student found with the name '{search_name}'")

    def search_instructor(self) -> None:
        instructor_name = input("Enter the name of the instructor you're searching for: ")
        for instructor in self.instructors:
            if instructor.name.lower() == instructor_name.lower():
                print(instructor)
                return instructor
        print(f"No instructor found with the name '{instructor_name}'")

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