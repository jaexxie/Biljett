class Person:
    def __init__(self, name: str, email: str, id_number: int):
        self.name = name
        self.email = email
        self.__id_number = id_number
        self.persons = []


    def get_id(self) -> int:
        return self.__id_number
    
    def __str__(self) -> str:
        return (f"\n Name: {self.name}, Email: {self.email}, ID: {self.__id_number} ")
