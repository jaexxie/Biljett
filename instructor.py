from person import Person

class Instructor(Person):
    def __init__(self, name: str, email:str, id_number: int, department: str):
        super().__init__(name, email, id_number)
        self.department = department
        self.courses_taught = []

    def assign_course(course):
        pass

    def list_courses():
        pass