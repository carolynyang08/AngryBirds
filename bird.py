from ball import *
import math
from cmu_112_graphics import *
from PIL import Image

bird_radius = 30

class Bird(Ball):
    STATES = ['resting', 'loaded', 'aiming', 'launched']
    def __init__(self, x, y, r, app):
        super().__init__(x, y, r, app)
        self.restingPosition = Vector(self.position.x, self.position.y)
        self.state = Bird.STATES[0]
        self.birdImage = app.loadImage('resources/images/red-bird3.png')
        #self.birdImage = app.scaleImage(tempImage, )


    def draw(self, canvas):
        pass
        #x, y = convert_coordinates(self.body.position)
        #canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.image1))
        # canvas.create_oval(int(x - app.ball_radius), int(y - app.ball_radius),
        # int(x + app.ball_radius), int(y + app.ball_radius), fill="yellow")