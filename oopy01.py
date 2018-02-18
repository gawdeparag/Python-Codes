class student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def marks_inc(self):
        if self.marks >= 29:
            self.marks = self.marks + 3
        else:
            return 0

student1 = student('ABC', 30)
student1.marks_inc()
print(student1.marks)

