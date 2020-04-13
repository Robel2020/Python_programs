class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student_count):
        self.name = name
        self.count = max_student_count
        self.students = []

    def add_student(self, name):
        if len(self.students) <= self.max_student_count:
            self.students.append(name)
            return True
        return

    def get_average(self):
        avr = 0
        for s in self.students:
            avr += s
        return avr/self.max_student_count

s1 = Students("Jhon", 23, 86)
s2 = Students("Sara", 25, 96)
s3 = Students("Ahmed", 21, 93)

course = Course("Math", 3)
course.add_student("Brown")
course.add_student("Takelle")
course.add_student("Hadish")

print(s1.get_grade())
print(s2.age)


