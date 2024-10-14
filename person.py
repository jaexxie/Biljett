
class Person:
    def __init__(self, name: str, email: str, id_number: int):
        self.name = name
        self.email = email
        self.__id_number = id_number


    def get_id(self):
        return self.__id_number
    
    def get_name(self):
        return self.name
    
    def display_details(self):
        return f"Name: {self.name}; Email: {self.email}, ID: {self.__id_number}"
    
    def add_person(self):
        pass

    def remove_person(self):
        pass 
    
person = Person("Jack", "Jack@gmail.com", 123)

print(person.display_details())