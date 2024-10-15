from course import Course
from instructor import Instructor
from student import Student
from enrollment import Enrollment

class Menu:
    def __init__(self):
        self.course = Course()

    def display_menu(self):

        while True:
            print("\nWelcome to school!")
            print("1) Add students")
            print("2) Hire instructors")
            print("3) Create course")
            print("4) List instructors")
            print("5) List students")
            print("6) List courses")
            print("7) Display enrollment details")
            print("8) Exit")


            choice = input("Your choice? ")

            if choice == "1":
                self.course.add_students()
            elif choice == "2":
                self.course.add_instructors()
            elif choice == "3":
                self.course.create_course()
            elif choice == "4":
                self.course.list_instructors()
            elif choice == "5":
                self.course.list_students()
            elif choice == "6":
                self.course.list_courses()
            elif choice == "7":
                self.enrollment.display_enrollment_details()
            elif choice == "8":
                print("\nSee you later!")
                break
            else:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()