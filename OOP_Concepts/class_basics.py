# Define a class Car
class Car:
    # Initialize instance variables with __init__() method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display car's details
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
