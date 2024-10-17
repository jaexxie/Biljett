
class Person:
    def __init__(self, name: str, email: str, id_number: int, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.name = name
        self.email = email
        self.__id_number = id_number

    def get_id(self) -> int:
        return self.__id_number