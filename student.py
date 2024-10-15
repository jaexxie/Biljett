from person import Person

class Student(Person):
    def __init__(self, name:str, email: str, id_number: int, major: str, course_name: str, course_code: str):
        super().__init__(name, email, id_number, course_name, course_code)
        self.__major = major
    
    def get_major(self):
        return self.__major