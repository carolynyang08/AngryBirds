from ball import *
import math
from rigidbody import *
from cmu_112_graphics import *
from PIL import Image

class Pig(Ball):
    def __init__(self, app, x, y, r):
        super().__init__(x, y, r, app)
        tempImage = app.loadImage('resources/images/pig_failed.png')
        self.pigImage = app.scaleImage(tempImage, .25)


    def draw(self, app, canvas):
        x, y = RigidBody.convert_coordinates((self.position.x, self.position.y), app.height)
        canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.pigImage))
        canvas.create_oval(x - self.r, y - self.r, x + self.r, y + self.r,
                           width=1, outline="black")

    def timerFired(self):
        self.move()


