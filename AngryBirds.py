import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d
from ground import *
from ball import *
from level import *
from bird import*



def appStarted(app):
    resetApp(app, 1)
    app.timerDelay = 50


def resetApp(app, level):
    app.birds = []
    app.pigs = []
    app.ground = Ground(app)
    app.boards = []
    app.slingshot = Slingshot(app.width//4, app)
    app.level = Level(app, app.birds, app.pigs, app.boards, app.ground, app.slingshot)
    app.level.goToLevel(level)
    app.stuffToRemove = []




def keyPressed(app, event):
    if event.key == "Right":
        app.bird.body.apply_force_at_local_point((15000000, 30000000), (0, 0))



def timerFired(app):
    app.space.step(1 / app.FPS)

    # app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)


def convert_coordinates(point):
    return point[0], 800 - point[1]


def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, 800, 800, fill="yellow")
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