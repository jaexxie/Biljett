from person import Person

class Student(Person):
    def __init__(self, name:str, email: str, id_number: int, major: str):
        super().__init__(name, email, id_number)
        self.major = major