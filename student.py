from person import Person

class Student(Person):
    all_students = []

    def __init__(self, name:str, email: str, id_number: int, major: str):
        super().__init__(name, email, id_number)
        self.__major = major
        self.courses = []

        Student.all_students.append(self)
    
    def get_major(self) -> str:
        return self.__major
    
    @classmethod
    def add_students(cls) -> "Student":
        name = input("Enter the student's name: ")
        email = input("Enter the student's email: ")
        id_number = int(input("Enter the student's ID number: "))
        major = input("Enter the student's major: ")


        student = cls(name, email, id_number, major)

        print(f"Student {name} has been created.")
        return student
    
    @classmethod
    def enroll(cls): 
        from course import Course
        student_name = input("Enter the student's name to enroll: ").strip()

        student = None
        for existing_student in cls.all_students:
            if existing_student.name.lower() == student_name.lower():
                student = existing_student
                break

        if student is None:
            print("Student not found. Please ensure the student has been created first.")
            return

        Course.list_courses()
        if Course.all_courses:
            course_name = input("Enter the name of the course to enroll in: ").strip()
            selected_course = None

            for course in Course.all_courses:
                if course.course_name.lower() == course_name.lower():
                    selected_course = course
                    break

            if selected_course:
                selected_course.students.append(student)
                student.courses.append(selected_course)
                print(f"Student '{student.name}' has been enrolled in '{selected_course.course_name}'.")
            else:
                print("Course not found.")
