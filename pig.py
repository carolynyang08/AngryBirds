from ball import *
import math
from rigidbody import *
from cmu_112_graphics import *
from PIL import Image

class Pig(Ball):
    STATES = 'resting', 'dead'
    def __init__(self, app, x, y, r, mass):
        super().__init__(app, x, y, r, mass)
        self.state = Pig.STATES[0]
        tempImage = app.loadImage('resources/images/pig_failed.png')
        self.pigImage = app.scaleImage(tempImage, 1/6)
        self.app = app
        self.initialHeight = self.position.y


    def draw(self, app, canvas):
        px, py = RigidBody.convert_coordinates((self.position.x, self.position.y), app.height)
        canvas.create_image(px, py, image = ImageTk.PhotoImage(self.pigImage))
        canvas.create_oval(px - self.r, py - self.r, px + self.r, py + self.r, width=1, outline="black")


    def timerFired(self):

        if self.state != Pig.STATES[0] and not self.isBalanced() or self.position.y > self.initialHeight + self.r:
            self.acceleration.y = RigidBody.GRAVITY
        else:
            self.acceleration.y = 0

        self.move()


    def isBalanced(self):

        for board in self.app.boards:
            if self.position.y == self.r:
                return True
            if (self.position.y >= board.position.y + self.r + min(board.width, board.height)/2 and
                self.position.y - board.position.y < self.r + min(board.width, board.height/2 + 3)):
                return True
            else:
                return False



