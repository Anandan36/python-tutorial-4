class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"Model: {self.model}, Year: {self.year}, Price: ₹{self.price}")

# Instances
car1 = Car("Honda City", 2020, 1200000)
car2 = Car("Tesla Model 3", 2023, 3500000)

car1.cost()
car2.cost()
