from person import Person

class Instructor(Person):
    def __init__(self, name: str, email:str, id_number: int, department: str, course_name: str, course_code: str):
        super().__init__(name, email, id_number, course_name, course_code)
        self.__department = department

    def get_department(self) -> str:
        return self.__department
    
    def __str__(self) -> str:
        return (f"Instructor Name: {self.name}, Email: {self.email}, ID: {self.get_id()}, Department: {self.get_department()}, Course: {self.course_name} ({self.course_code})")