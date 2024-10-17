class Course():
    all_courses = []

    def __init__(self, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.instructors = []

        Course.all_courses.append(self)

    @classmethod
    def create_course(cls) -> None:
        course_name = input("Enter course name: ")
        course_code = input("Enter course code: ")

        cls(course_name, course_code)
        print(f"Course '{course_name}' has been added to the list of courses.")
    
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

    @classmethod
    def list_courses(cls) -> None:
        if not cls.all_courses:
            print("No courses have been created yet.")
        else:
            for course in cls.all_courses:
                print(f"Course name: {course.course_name}, Course Code: {course.course_code}")

    @classmethod
    def display_enrollment_details(cls) -> None:
        course_name = input("Enter the course name")

        course_found = False

        for course in cls.all_courses:
            if course.course_name.lower() == course_name.lower():

                course_found = True

                print(f"Course Name: {course.course_name}, Course Code: {course.course_code}")

                print("\nInstructors")
                if not course.instructors:
                    print("No instructors assigned")
                else:
                    for instructor in course.instructors:
                        print(f"Name: {instructor.name}, Email: {instructor.email}")
                
                print("\nStudents")
                if not course.students:
                    print("No students enrolled to the course")
                else:
                    for student in course.students:
                        print(f"Name: {student.name}")
                        break
        if not course_found:
            print("No course found")
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''def display_enrollment_detail(self) -> None:
            
        #Course name, Instructor, All the students assigned to that course
        course_name = input("Enter the course: ")

        course_found = None

        for course in self.courses:
            if course.course_name == course_name:
                course_found = course
                break


        if course_found:
            print(f"Name: {course_found.course_name}")

            print("Instructors:")

            if not course_found.instructors:
                print("No instructors assigned yet")
            else:
                for instructor in course_found.instructors:
                    print(f"Name: {instructor.name}")
                
            print("Students")

            if not course_found.students:
                print("No students enrolled to the course yet")
            else:
                for student in course_found.students:
                    print(f"Name: {student.name}")
        else:
            print("Course not found")
            '''


                

