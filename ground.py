import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d

class Ground():
    def __init__(self, app):
        self.backgroundImage = app.loadImage('resources/images/background3.png')

    def draw(self, app, canvas):
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(self.backgroundImage))


