from person import Person

class Student(Person):
    def __init__(self, name:str, email: str, id_number: int, major: str, grade = None):
        super().__init__(name, email, id_number)
        self.major = major
        self.grade = grade
    
    def display_grades(self):
        pass