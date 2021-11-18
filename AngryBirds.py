import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d
from ground import *
from ball import *
from level import *
from bird import*
from slingshot import *


def appStarted(app):
    resetApp(app, 1)
    app.timerDelay = 50


def resetApp(app, level):
    app.birds = []
    app.pigs = []
    app.ground = Ground(app)
    app.boards = []
    app.slingshot = Slingshot(app, app.width//4)
    app.level = Level(app, app.birds, app.pigs, app.boards, app.ground, app.slingshot)
    app.level.goToLevel(1)
    app.stuffToRemove = []



def keyPressed(app, event):
    pass

def mouseDragged(app, event):
    if app.birds:
        app.birds[0].mouseDragged(event)

def mouseReleased(app, event):
    if app.birds:
        app.birds[0].mouseReleased(event)



def timerFired(app):
    for bird in app.birds:
        bird.timerFired()
    for pig in app.pigs:
        pig.timerFired()



def convert_coordinates(point, app):
    return point[0], app.height - point[1]


def redrawAll(app, canvas):
    app.ground.draw(app, canvas)
    app.slingshot.draw(app, canvas)
    for pig in app.pigs:
        pig.draw(app, canvas)
    for bird in app.birds:
        bird.draw(app, canvas)



runApp(width=1440, height=718)


