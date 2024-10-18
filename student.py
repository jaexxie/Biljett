from person import Person

class Student(Person):
    def __init__(self, name:str, email: str, id_number: int, major: str, course_name: str, course_code: str):
        super().__init__(name, email, id_number, course_name, course_code)
        self.__major = major
    
    def get_major(self) -> str:
        return self.__major
    
    def __str__(self) -> str:
        return (f"Student Name: {self.name}, Email: {self.email}, ID: {self.get_id()}, Major: {self.get_major()}, Course: {self.course_name} ({self.course_code})")