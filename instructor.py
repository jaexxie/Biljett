from person import Person

class Instructor(Person):
    all_instructors = []

    def __init__(self, name: str, email:str, id_number: int, department: str):
        super().__init__(name, email, id_number)
        self.__department = department
        self.courses = []
        Instructor.all_instructors.append(self)

    def get_department(self) -> str:
        return self.__department

    @classmethod
    def add_instructors(cls) -> None:
        name = input("Enter the instructor's name: ")
        email = input("Enter the instructor's email: ")
        id_number = int(input("Enter the instructor's ID number: "))
        department = input("Enter the instructor's department: ")

        instructor = cls(name, email, id_number, department)

        print(f"Instructor {name} has been added.")
        return instructor

    @classmethod
    def assign(cls): 
        from course import Course
        instructor_name = input("Enter the instructor's name: ")

        instructor = None
        for existing_instructor in cls.all_instructors:
            if existing_instructor.name.lower() == instructor_name.lower():
                instructor = existing_instructor
                break

        if instructor is None:
            print("Instructor is not found")
            return
        
        Course.list_courses
        if Course.all_courses:
            course_name = input("Enter the name of the course: ").strip()
            selected_course = None

            for course in Course.all_courses:
                if course.course_name.lower() == course_name.lower():
                    selected_course = course
                    break
            if selected_course:
                selected_course.instructors.append(instructor)
                instructor.courses.append(selected_course)
                print(f"Instructor '{instructor.name}' has been assigned to '{selected_course.course_name}'.")
            else:
                print("Course not found.")
