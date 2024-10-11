from course import Course

class Enrollment(Course):
    def __init__(self, course_name: str, course_code: str, instructor, grade:float, semester: str):
        super().__init__(course_name, course_code, instructor)
        self.grade = grade
        self.semester = semester