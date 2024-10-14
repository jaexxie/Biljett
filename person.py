class Person:
    def __init__(self, name: str, email: str, id_number: int):
        self.name = name
        self.email = email
        self.__id_number = id_number
        self.persons = []


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
    
person_manage = Person("Manager", "Manager@example.com", 123)

person_manage.add_person()


#from instructor import Instructor
 #       from student import Student
  #      
    #    who = input("Would you like to add student or instructor: ")

     #   if who.lower() == "instructor":
      #      name = input("Enter the instructors's name: ")
       #     email = input("Enter the instructor's email: ")
        #    id = int(input("Enter the instructor's ID number: "))
         #   department = input("Enter the instructor's department: ")

          #  person = Instructor(name, email, id, department)

        #elif who.lower() == "student":
         #   name = input("Enter the student's name: ")
          #  email = input("Enter the student's email: ")
           # id = int(input("Enter the student's ID number: "))
            #major = input("Enter student's major: ")

            #person = Student(name, email, id, major) 
        
        #else:
         #   print("Invalid option. Please choose either 'student' or 'instructor'.")
          #  return
        
        
        #self.persons.append(person)