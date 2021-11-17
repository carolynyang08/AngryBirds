import pymunk
import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d

bird_radius = 30


class Bird():
    def __init__(self, app):
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


class Pig():
    def __init__(self, app, x, y, radius, image):
        self.pig_radius = radius
        self.body = pymunk.Body(7)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, self.pig_radius)
        self.shape.density = 1
        self.shape.elasticity = 0.8
        self.shape.collision_type = 3
        app.space.add(self.body, self.shape)
        self.image1 = app.scaleImage(image, 2 * (self.pig_radius / image.size[0]))
        # app.bird.sprites = []

    def draw(self, canvas):
        x, y = convert_coordinates(self.body.position)
        canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.image1))
        # canvas.create_oval(int(x - app.ball_radius), int(y - app.ball_radius),
        # int(x + app.ball_radius), int(y + app.ball_radius), fill="yellow")


class Wood():
    def __init__(self, app, x, y, length, height, image):
        self.body = pymunk.Body(7, 10000)
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (length, height))
        self.shape.density = 1
        self.shape.elasticity = 0.8
        self.shape.friction = 0.8
        self.shape.collision_type = 1
        app.space.add(self.body, self.shape)
        self.image = image
        # self.image1 = app.scaleImage(image, .25)
        # app.bird.sprites = []

    def draw(self, canvas):
        x, y = convert_coordinates(self.body.position)
        angle = math.degrees(self.body.angle)
        self.image = self.image.rotate(angle)
        canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.image))
        '''offset = Vec2d(*self.image.get_size())/2.
        newposition = Vec2d(x, y) - offset
        canvas.create_image(int(newposition[0]), int(newposition[1]), image=ImageTk.PhotoImage(self.image))'''


class Slingshot():
    def __init__(self, app):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.position = (50, 265), (150, 265)
        self.shape = pymunk.Segment(self.body, (50, 265), (150, 265), 5)
        app.space.add(self.body, self.shape)

    def draw(self, canvas):
        startx, starty = convert_coordinates(self.position[0])
        endx, endy = convert_coordinates(self.position[1])
        canvas.create_line(startx, starty, endx, endy, fill="black", width=12)


class Floor():
    def __init__(self, app):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.position = (150, 45), (800, 45)
        self.shape = pymunk.Segment(self.body, (150, 45), (800, 45), 6)
        self.shape.elasticity = .8
        app.space.add(self.body, self.shape)

    def draw(self, canvas):
        startx, starty = convert_coordinates(self.position[0])
        endx, endy = convert_coordinates(self.position[1])
        canvas.create_line(startx, starty, endx, endy, fill="black", width=18)


def appStarted(app):
    app.space = pymunk.Space()
    app.timerDelay = 50
    app.FPS = 1000 / app.timerDelay
    app.space.gravity = 0, -1000

    '''blackbirdurl = 'https://www.angrybirdsnest.com/wp-content/uploads/hm_' \
          'bbpui/218718/fn7w2do1f6e4q2si7e6zd4fmgnas9hae.png

    spritestrip = app.loadImage(blackbirdurl)

    for i in range(2):
        sprite = spritestrip.crop((321*i, 321, 0, 420))
        app.sprites.append(sprite)
        app.spriteCounter = 0'''

    birdUrl = 'https://www.freeiconspng.com/thumbs/angry-birds-png/' \
              'angry-birds-png-images-free-download-1.png'
    app.birdImage = app.loadImage(birdUrl)

    smilyPigUrl = 'https://i.pinimg.com/originals/c2/2d/03/c22d033f26f' \
                  'a2d329951849c8d9c4329.png'
    app.pig1Image = app.loadImage(smilyPigUrl)

    app.woodplank1Image = app.loadImage('woodplank.png')
    app.woodplank1Image = app.scaleImage(app.woodplank1Image, .25)
    (app.woodplank1x, app.woodplank1y) = app.woodplank1Image.size

    app.woodplank2Image = app.loadImage('woodplank.png')
    app.woodplank2Image = app.scaleImage(app.woodplank2Image, .25)
    (app.woodplank2x, app.woodplank2y) = app.woodplank2Image.size


    app.bird = Bird(app)
    app.slingshot = Slingshot(app)
    app.floor = Floor(app)
    app.pig = Pig(app, 550, 80, 30, app.pig1Image)
    app.woodplank1 = Wood(app, 475, 51 + int(.5 * app.woodplank1y), \
                          app.woodplank1x, app.woodplank1y, app.woodplank1Image)
    app.woodplank2 = Wood(app, 625, 51 + int(.5 * app.woodplank2y), \
                          app.woodplank2x, app.woodplank2y, app.woodplank2Image)



def keyPressed(app, event):
    if event.key == "Right":
        app.bird.body.apply_force_at_local_point((15000000, 30000000), (0, 0))


def timerFired(app):
    app.space.step(1 / app.FPS)

    # app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)


def convert_coordinates(point):
    return point[0], 800 - point[1]


def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, 800, 800, fill="white")
    app.bird.draw(canvas)
    app.slingshot.draw(canvas)
    app.floor.draw(canvas)
    app.pig.draw(canvas)
    app.woodplank1.draw(canvas)
    app.woodplank2.draw(canvas)


def playAngryBirds():
    runApp(width=800, height=800)


def main():
    playAngryBirds()


main()