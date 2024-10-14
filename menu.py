from enrollment import Enrollment
class Menu:
    def __init__(self):
        self.enrollment = None

    def display_menu(self):

        while True:
            print("\nWelcome to school!")
            print("1) Add students")
            print("2) Hire instructors")
            print("3) Create course")
            print("4) Enroll student")
            print("5) List instructors")
            print("6) List students")
            print("7) List courses")
            print("8) Display enrollment details")
            print("9) Exit")


            choice = input("Your choice? ")

            if choice == "1":
                self.enrollment.add_student()
            elif choice == "2":
                self.enrollment.hire_instructor()
            elif choice == "3":
                self.enrollment.create_course()
            elif choice == "4":
                self.enrollment.enroll_student()
            elif choice == "5":
                self.enrollment.list_instructors()
            elif choice == "6":
                self.enrollment.list_students()
            elif choice == "7":
                self.enrollment.list_courses()
            elif choice == "8":
                self.enrollment.display_enrollment_details()
            elif choice == "9":
                print("\nSee you later!")
                break
            else:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()


