class Arith:
    def read(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b if self.b != 0 else "Division by zero!"

# Example
obj = Arith()
obj.read(10, 5)
print("Sum:", obj.add())
print("Difference:", obj.subtract())
print("Product:", obj.multiply())
print("Quotient:", obj.divide())
