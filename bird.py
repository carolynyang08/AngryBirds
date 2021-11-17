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
        self.birdImage = app.loadImage(app, 'resources/images/red-bird3.png')
        #self.birdImage = app.scaleImage(tempImage, )








        self.body = pymunk.Body(10)
        self.body.position = 100, 300
        self.shape = pymunk.Circle(self.body, bird_radius)
        self.shape.density = 1
        self.shape.elasticity = 0.8
        self.shape.collision_type = 2
        app.space.add(self.body, self.shape)
        self.image1 = app.scaleImage(app.birdImage, 2 * (bird_radius / app.birdImage.size[0]))
        # app.bird.sprites = []

    def draw(self, canvas):
        x, y = convert_coordinates(self.body.position)
        canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.image1))
        # canvas.create_oval(int(x - app.ball_radius), int(y - app.ball_radius),
        # int(x + app.ball_radius), int(y + app.ball_radius), fill="yellow")