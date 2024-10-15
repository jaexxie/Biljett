from person import Person

class Instructor(Person):
    def __init__(self, name: str, email:str, id_number: int, department: str, course_name: str, course_code: str):
        super().__init__(name, email, id_number, course_name, course_code)
        self.__department = department

    def get_department(self):
        return self.__department