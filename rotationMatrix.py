import math
from vector import *

class RotationMatrix():

    def __init__(self, angle):
        self.angle = angle

    def multiply(self, vec):
        return Vector(math.cos(self.angle) * vec.x - math.sin(self.angle) * vec.y,
                      math.sin(self.angle) * vec.x + math.cos(self.angle) * vec.y)