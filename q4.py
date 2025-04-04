class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def dataprint(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}")

# Instances
s1 = Student("Anjali", 101)
s2 = Student("Rahul", 102)

s1.dataprint()
s2.dataprint()
