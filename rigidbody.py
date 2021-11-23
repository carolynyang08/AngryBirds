from vector import *

class RigidBody():
    GRAVITY = -9.8
    PIXELS_PER_METER = 10

    def __init__(self, x, y, elasticity):
        self.position = Vector(x, y)
        self.elasticity = elasticity
        self.mass = 0
        self.inverse_mass = 0
        self.inertia = 0
        self.inverse_inertia = 0
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.angle = 0
        self.angularVelocity = 0
        self.friction = 0


    @staticmethod
    def convert_coordinates(point, screenHeight):
        return point[0], screenHeight - point[1]


