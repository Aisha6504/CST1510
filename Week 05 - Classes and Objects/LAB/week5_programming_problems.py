''' Week 5 – Classes and Objects – Programming Problems

## Task 1: Student Class

Create a class `Student` with attributes `name` and `age` set in `__init__`. 
Create two student objects and print their attributes using dot notation.'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Aisha", 18)
student2 = Student("John", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)

'''## Task 2: Gradebook

Create a class `Course` that stores a course name and a list of `Student` 
objects (each with a name and a list of marks). Add methods `add_student()`,
 `average_mark(student_name)` and `top_student()`. 
 Create a course with at least 4 students and print each student's average and the top student.'''
print("task 2")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_mark(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return sum(student.marks) / len(student.marks)

    def top_student(self):
        top = self.students[0]

        for student in self.students:
            if sum(student.marks) / len(student.marks) > sum(top.marks) / len(top.marks):
                top = student

        return top


course = Course("Programming")

course.add_student(Student("Aisha", [80, 75, 90]))
course.add_student(Student("John", [70, 65, 60]))
course.add_student(Student("Mary", [95, 90, 92]))
course.add_student(Student("Ahmed", [85, 80, 88]))

for student in course.students:
    average = course.average_mark(student.name)
    print(f"{student.name}: {average:.2f}")

top = course.top_student()
top_average = course.average_mark(top.name)

print(f"\nTop student: {top.name} ({top_average:.2f})")
