import math

class Shape:

    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side_length) -> None:
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2