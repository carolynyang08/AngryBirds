from cmu_112_graphics import *
from rigidbody import *
from bird import *
from PIL import Image

class Slingshot():
    STATES = ['rest', 'pulled']
    MAX = 125
    def __init__(self, app, x):
        self.slingshotImage = app.loadImage('resources/images/sling.png')
        self.imageWidth, self.imageHeight = self.slingshotImage.size
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
        self.app = app

    def mouseDragged(self, bird):
        if bird.state == bird.STATES[1]:
            self.state = Slingshot.STATES[1]
            self.centerx, self.centery = bird.position.x, bird.position.y

    def draw(self, app, canvas):
        canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(self.slingshotImage))
        if self.state == Slingshot.STATES[1]:
            x, y = RigidBody.convert_coordinates((self.centerx, self.centery), app.height)
            canvas.create_line(x, y, self.slingX1, self.slingY1, fill="#410E02", width=4)
            canvas.create_line(x, y, self.slingX2, self.slingY2, fill="#410E02", width=4)



