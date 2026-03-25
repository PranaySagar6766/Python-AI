import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def describe(self):
        print(f"Area of {type(self).__name__}: {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(7) ,Rectangle(10,15) , Circle(55)]
for shape in shapes:
    shape.describe()