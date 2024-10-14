
class Person:
    def __init__(self, name: str, email: str, id_number: int):
        self.name = name
        self.email = email
        self.__id_number = id_number


    def get_id(self):
        return self.__id_number
    
    def __str__(self):
        return (f"\n Name: {self.name}, Email: {self.email}, ID: {self.__id_number} ")