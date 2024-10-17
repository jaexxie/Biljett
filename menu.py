from course import Course
from student import Student
from instructor import Instructor

class Menu:
    def display_menu(self) -> None:

        while True:
            print("\nWelcome to school!")
            print("1) Create course")
            print("2) Add student")
            print("3) Enroll student into the course")
            print("4) Create instructor")
            print("5) Assign instructor to the course")
            print("6) List courses")
            print("7) Display enrollment details")
            print("8) Exit")


            choice = input("Your choice? ")

            if choice == "1":
                Course.create_course()  
            elif choice == "2":
                Student.add_students()  
            elif choice == "3":
                Student.enroll()  
            elif choice == "4":
                Instructor.add_instructors()  
            elif choice == "5":
                Instructor.assign()  
            elif choice == "6":
                Course.list_courses()  
            elif choice == "7":
                Course.display_enrollment_details()  
            elif choice == "8":
                print("\nGoodbye!")
                break
            else:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()