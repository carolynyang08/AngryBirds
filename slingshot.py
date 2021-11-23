from cmu_112_graphics import *
from rigidbody import *
from bird import *
from PIL import Image

class Slingshot():
    STATES = ['rest', 'pulled']
    MAX = 100
    BANDWIDTH = 10
    def __init__(self, app, x):
        slingshotImage = app.loadImage('resources/images/sling.png')
        self.slingimage = app.scaleImage(slingshotImage, 1/2)
        self.imageWidth, self.imageHeight = self.slingimage.size
        self.x = x
        self.y = self.imageHeight//2
        self.slingX1, self.slingY1 = (self.x - 20, self.y + 30)
        self.slingX2, self.slingY2 = (self.x + 10, self.y + 30)
        self.state = Slingshot.STATES[0]
        self.px, self.py = RigidBody.convert_coordinates((self.x, self.y), app.height)
        self.centerx, self.centery = ((self.slingX1 + self.slingX2) // 2, self.slingY1)
        self.color = '#410E02'

        '''slingshotImage = app.loadImage('resources/images/sling.png')
        self.slingimage = app.scaleImage(slingshotImage)
        self.imageWidth, self.imageHeight = self.slingshotImage.size
        self.x = x
        self.y = self.imageHeight // 2
        self.slingX1, self.slingY1 = (self.x - 30, self.y + 70)
        self.slingX2, self.slingY2 = (self.x + 10, self.y + 70)
        self.state = Slingshot.STATES[0]
        self.px, self.py = RigidBody.convert_coordinates((self.x, self.y), app.height)'''

    def mouseDragged(self, bird):
        if bird.state == bird.STATES[2]:
            self.state = Slingshot.STATES[1]
            self.centerx, self.centery = bird.position.x, bird.position.y

    def mouseReleased(self, bird):
        self.state = Slingshot.STATES[0]
        self.centerx, self.centery = (self.slingX1 + self.slingX2) // 2, self.slingY1


    def draw(self, app, canvas):
        canvas.create_image(self.px, self.py, image=ImageTk.PhotoImage(self.slingimage))
        x, y = RigidBody.convert_coordinates((self.centerx, self.centery), app.height)
        convSlingX1, convSlingY1 = RigidBody.convert_coordinates((self.slingX1, self.slingY2), app.height)
        convSlingX2, convSlingY2 = RigidBody.convert_coordinates((self.slingX2, self.slingY2), app.height)

        if self.state == Slingshot.STATES[0]:
            canvas.create_line(convSlingX1, convSlingY1, convSlingX2, convSlingY2, \
                               fill=self.color, width=Slingshot.BANDWIDTH)
        if self.state == Slingshot.STATES[1]:
            canvas.create_line(x, y, convSlingX1, convSlingY1, fill=self.color, width=Slingshot.BANDWIDTH)
            canvas.create_line(x, y, convSlingX2, convSlingY2, fill=self.color, width=Slingshot.BANDWIDTH)







