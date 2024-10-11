
class Course:
    def __init__(self, course_name: str, course_code: str, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []