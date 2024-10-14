from person import Person

class Student(Person):
    def __init__(self, name:str, email: str, id_number: int, major: str):
        super().__init__(name, email, id_number)
        self.major = major
        self.courses_enrolled = []

    def enroll(course):
        pass

    def list_enrollments():
        pass