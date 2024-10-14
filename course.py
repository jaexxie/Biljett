
class Course:
    def __init__(self, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructors = []
        self.students = []
        
    