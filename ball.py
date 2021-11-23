from rigidbody import *
import math
from cmu_112_graphics import *
from rigidbody import *
from vector import *
from PIL import Image


class Ball(RigidBody):

    def __init__(self, app, x, y, r, mass):
        super().__init__(x, y, .5)
        self.app = app
        self.r = r
        self.mass = mass
        if self.mass == 0:
            self.inverse_mass = 0
        else:
            self.inverse_mass = 1/self.mass
        # CITATION: I got the formula from https://ocw.mit.edu/courses/mechanical-engineering/2-003j-dynamics-and-control-i-spring-2007/lecture-notes/lec11.pdf
        self.inertia = self.mass * (self.r/RigidBody.PIXELS_PER_METER)**2/2
        if self.inertia == 0:
            self.inverse_inertia = 0
        else:
            self.inverse_inertia = 1/self.inertia

    def move(self):
        # CITATIONS: I got the equations from:
        # https://www.physicsclassroom.com/class/1DKin/Lesson-6/Kinematic-Equations
        # #xf = x0 + v0*t + .5*a*t^2
        # vf = v0 + at
        self.position = (self.position / RigidBody.PIXELS_PER_METER + self.velocity) * RigidBody.PIXELS_PER_METER
        self.velocity = self.velocity + self.acceleration
        if self.position.x < self.r or self.position.x > self.app.width - self.r:
            self.state == 'dead'



