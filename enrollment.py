from instructor import Instructor
from student import Student
from course import Course

'''class Enrollment(Course):
    def __init__(self, course_name: str, course_code: str):
        super().__init__(course_name, course_code)

    def display_enrollment_details(self):
        
        #Course name, Instructor, All the students assigned to that course
        course_name = input("Enter the course: ")

        if course_name in self.courses:
            for course in Course.all_courses:
                if course.course_name == course_name:
                    print(f"Course name: {course.course_name}")

                    print("Instructors: ")
                    if not course.instructors:
                        print("No instructors")
                    else:
                        for instructor in course.instructors:
                            print(f"Name: {instructor.name}, Email: {instructor.email}")

                    print("Students")
                    if not course.students:
                        print("No students")
                    else:
                        for student in course.students:
                            print(f"Name: {student.name}, Email: {student.email}")
                    break
        else:
            print("Course not found")        '''