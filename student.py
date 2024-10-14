from person import Person

class Student(Person):
    def __init__(self, name:str, email: str, id_number: int, course_name: str, course_code: str, major: str):
        super().__init__(name, email, id_number, course_name, course_code)
        self.major = major