from person import Person

class Instructor(Person):
    def __init__(self, name: str, email:str, id_number: int, department: str):
        super().__init__(name, email, id_number)
        self.department = department

    def assign_course(self):
        pass

    def list_courses(self):
        pass