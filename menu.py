from course import Course
from instructor import Instructor
from student import Student

class Menu:
    def __init__(self):
        self.course = Course()

    def display_menu(self) -> None:

        while True:
            print("\nWelcome to school!")
            print("1) Add student")
            print("2) Hire instructor")
            print("3) Delete student")
            print("4) Delete instructor")
            print("5) List students")
            print("6) List instructors")
            print("0) Exit")


            choice = input("Your choice? ")

            if choice == "1":
                self.course.add_students()
            elif choice == "2":
                self.course.add_instructors()
            elif choice == "3":
                self.course.delete_student()
            elif choice == "4":
                self.course.delete_instructor()
            elif choice == "5":
                self.course.list_students()
            elif choice == "6":
                self.course.list_instructors()
            elif choice == "0":
                print("\nSee you later!")
                break
            else:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()