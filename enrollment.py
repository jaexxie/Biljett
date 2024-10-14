from course import Course

class Enrollment(Course):
    def __init__(self, course_name: str, course_code: str, instructor, grade:float):
        super().__init__(course_name, course_code, instructor)
        self.__grade = grade

    def get_grade(self):
        return self.__grade
    
    def add_student(self) -> str:
        pass

    def add_instructor(self) -> str:
        pass

    def create_course(self) -> str:
        pass

    def enroll_student(self) -> str:
        pass

    def list_instructors(self) -> str:
        pass

    def list_students(self) -> str:
        pass

    def list_courses(self) -> str:
        pass

    def display_enrollment_details(self):
        pass


    