from person import Person

class Instructor(Person):
    def __init__(self, name: str, email:str, id_number: int, department: str, courses_assigned = None):
        super().__init__(name, email, id_number)
        self.department = department
        self.courses_assigned = courses_assigned

    def assign_course(self):
        pass