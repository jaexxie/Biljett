
class Person:
    def __init__(self, name: str, email: str, id_number: int):
        self.name = name
        self.email = email
        self.__id_number = id_number


    def get_id(self):
        return self.__id_number
    
    def __str__(self):
        return (f"\n{self.name} takes the course {self.course_code}, {self.course_name}")
    

student = Person("Alex", "123@gmail.com", 14, "Object Oriented Programming", "DA361A")

print(student)