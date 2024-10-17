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
            print("3) Create course")
            print("4) Delete student")
            print("5) Delete instructor")
            print("6) Delete course")
            print("7) List instructors")
            print("8) List students")
            print("9) List courses")
            print("10) Display enrollment details")
            print("0) Exit")


            choice = input("Your choice? ")

            if choice == "1":
                self.course.add_students()
            elif choice == "2":
                self.course.add_instructors()
            elif choice == "3":
                self.course.create_course()
            elif choice == "4":
                self.course.delete_student()
            elif choice == "5":
                self.course.delete_instructor()
            elif choice == "6":
                self.course.delete_course()
            elif choice == "7":
                self.course.list_students()
            elif choice == "8":
                self.course.list_instructors()
            elif choice == "9":
                self.course.list_courses()
            elif choice == "10":
                self.course.display_enrollment_details()
            elif choice == "0":
                print("\nSee you later!")
                break
            else:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()