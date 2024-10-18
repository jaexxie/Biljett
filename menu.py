from course import Course
from instructor import Instructor
from student import Student

class Menu:
    def __init__(self):
        self.course = Course()

    def display_menu(self) -> None:
        """
        Displays the menu options for managing students and instructors,
        """

        while True:
            print("\nWelcome to school!")
            print("1) Add student")
            print("2) Hire instructor")
            print("3) Delete student")
            print("4) Delete instructor")
            print("5) Update student")
            print("6) Update instructor")
            print("7) Search student")
            print("8) Search instructor")
            print("9) List students")
            print("10) List instructors")
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
                self.course.update_student()
            elif choice == "6":
                self.course.update_instructor()
            elif choice == "7":
                self.course.search_student()
            elif choice == "8":
                self.course.search_instructor()
            elif choice == "9":
                self.course.list_students()
            elif choice == "10":
                self.course.list_instructors()
            elif choice == "0":
                print("\nSee you later!")
                break
            else:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()