from rigidbody import *
import math
from cmu_112_graphics import *
from rigidbody import *
from vector import *
from PIL import Image

#
class Ball(RigidBody):

    ELASTICITY = 0.5
    FRICTION = 0.5

    def __init__(self, x, y, r, app):
        self.app = app
        self.position = Vector(x, y)
        self.r = r
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def move(self):
        #xf = x0 + v0*t + .5*a*t^2
        self.position = self.position + self.velocity + self.acceleration * .5
        #vf = v0 + at
        self.velocity = self.velocity + self.acceleration
        if self.position.x <= 0 or self.position.x >= self.app.width:
            self.state == 'dead'



