# Define a class Rectangle
class Rectangle:
    # Initialize instance variables
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # Property method to calculate area
    @property
    def area(self):
        return self._length * self._width

    # Property method to calculate perimeter
    @property
    def perimeter(self):
        return 2 * (self._length + self._width)

    # Dunder method to return a string representation
    def __str__(self):
        return f"Rectangle(Length: {self._length}, Width: {self._width})"

    # Dunder method to compare two rectangles
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.area == other.area

Create two rectangle instances
rect1 = Rectangle(5, 3)
rect2 = Rectangle(3, 5)

Demonstrate the use of all methods
print(rect1)
print(f"Area: {rect1.area}, Perimeter: {rect1.perimeter}")
print(rect2)
print(f"Area: {rect2.area}, Perimeter: {rect2.perimeter}")
print(f"Are rect1 and rect2 equal? {rect1 == rect2}")
