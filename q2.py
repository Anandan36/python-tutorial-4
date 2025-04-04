class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example
rect = Rectangle(10, 5)
print("Area of rectangle:", rect.area())
