
class Person:
    def __init__(self, name: str, email: str, id_number: int, course_name: str, course_code: str):
        self.name = name
        self.email = email
        self.__id_number = id_number
        self.course_name = course_name
        self.course_code = course_code

    def get_id(self):
        return self.__id_number
    
    def __str__(self):
        return "{self.name}: takes the course {self.course_code}, {self.course_name}"
    

student = Student("Alex", "")