from student import Student
from course import Course

class Enrollment(Course):
    def __init__(self, course_name: str, course_code: str, grade:float):
        super().__init__(course_name, course_code)
        self.__grade = grade

    def get_grade(self):
        return self.__grade


    