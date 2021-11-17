from cmu_112_graphics import *
from rigidbody import *
from PIL import Image

class Slingshot():
    STATES = ['rest', 'pulled']
    max = 100
    def __init__(self, app, x):
        self.slingshotImage = app.loadImage('resources/images/sling.png')
        self.imageWidth, self.imageHeight = self.slingshotImage.size()
        self.x = x
        self.y = self.imageHeight//2
        self.slingX1, self.slingY1 = RigidBody.convert_coordinates((self.x - 30,\
                                                                    self.y + 70), app.height)
        self.slingX2, self.slingY2 = RigidBody.convert_coordinates((self.x + \
                                                                    10, self.y + 70), app.height)
        self.state = Slingshot.STATES[0]
        self.px, self.py = RigidBody.convert_coordinates((self.x, self.y), app.height)
        self.centerx, self.centery = (self.slingX1 + self.slingX2) // 2, self.slingY1
        self.color = 'brown'




    def draw(self, app, canvas):
        canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(self.slingshotImage))
        if self.state == 'pulled':
