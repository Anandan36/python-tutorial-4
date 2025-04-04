class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ₹{self.salary}")

p1 = Person("Meera", 28, 50000)
p2 = Person("Arun", 35, 70000)

p1.display()
p2.display()
