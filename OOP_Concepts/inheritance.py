# Parent class Employee
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")

Child class Manager that inherits from Employee
class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)  # Initialize inherited attributes
        self.department = department

    def get_details(self):
        super().get_details()  # Call the parent's get_details() method
        print(f"Department: {self.department}")

Create instances of both classes
employee = Employee("vicky", "Software Engineer")
manager = Manager("Kiss", "Team", "IT Department")

Call get_details() for each
print("Employee Details:")
employee.get_details()

print("\nManager Details:")
manager.get_details()

