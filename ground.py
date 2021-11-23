import math
from cmu_112_graphics import *
from rigidbody import *
from vector import *
from PIL import Image
from pymunk.vec2d import Vec2d

class Ground(RigidBody):
    def __init__(self, app):
        super().__init__(app.width/2, 0, app.width)
        self.backgroundImage = app.loadImage('resources/images/background3.png')
        self.width = app.width
        self.vertices = []
        self.vertices.append(Vector(0, 0))
        self.vertices.append(Vector(app.width, 0))
        self.orientation = (self.vertices[1] - self.vertices[0]).unit()


    def draw(self, app, canvas):
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(self.backgroundImage))


