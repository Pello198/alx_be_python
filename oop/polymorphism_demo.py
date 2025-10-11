# polymorphism_demo.py

import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Method to calculate area. Must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Rectangle shape derived from Shape."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape derived from Shape."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * self.radius ** 2
