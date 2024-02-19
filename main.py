class Person:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name

    def display_details(self):
        print(f"ID: {self._student_id}, Name: {self._name}")


class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self._grades = {}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self._grades[subject] = grade
        else:
            print("Invalid grade. Grade should be between 0 and 100.")

    def average_grade(self):
        if self._grades:
            return sum(self._grades.values()) / len(self._grades)
        else:
            return 0

    def display_details(self):
        super().display_details()
        print(f"Average Grade: {self.average_grade()}")


class StudentManagementSystem:
    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def show_student_details(self, student_id):
        for student in self._students:
            if student._student_id == student_id:
                student.display_details()
                return
        print(f"Student with ID {student_id} not found.")

    def show_student_average_grade(self, student_id):
        for student in self._students:
            if student._student_id == student_id:
                print(f"Average Grade for Student ID {student_id}: {student.average_grade()}")
                return
        print(f"Student with ID {student_id} not found.")


# Example usage:
# Creating instances of Student and StudentManagementSystem
student1 = Student(student_id=1, name="John Doe")
student2 = Student(student_id=2, name="Jane Smith")

sms = StudentManagementSystem()

# Adding students to the system
sms.add_student(student1)
sms.add_student(student2)

# Adding grades for students
student1.add_grade("Math", 90)
student1.add_grade("History", 85)
student2.add_grade("Math", 75)
student2.add_grade("History", 80)

# Displaying student details and average grades
sms.show_student_details(1)
sms.show_student_average_grade(1)
sms.show_student_details(2)
sms.show_student_average_grade(2)
