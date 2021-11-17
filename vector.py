import math
import numbers
import operator


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def dot(self, other):
        return self.x * other.x + self.y + other.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def unit(self):
        if self.magnitude() == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x/self.magnitude(), self.y/self.magnitude())




