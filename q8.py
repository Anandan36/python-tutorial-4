class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: ₹{self.cost}")

b = Book()
b.get_details("Python for Beginners", "James Smith", 499)
b.print_details()
