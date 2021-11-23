from cmu_112_graphics import *
import math, copy, os
import tkinter as tk
from bird import *
from pig import *
from slingshot import *
from level import *
from physics_engine import *
from ground import *


def splashScreenMode_redrawAll(app, canvas):
    font = 'Consolas 26 bold italic'
    canvas.create_text(app.width / 2, 150, text='Welcome to Angry Birds!', font=font, fill="YellowGreen")
    canvas.create_text(app.width / 2, 250, text='Press any key to start the game!', font=font, fill="YellowGreen")


def splashScreenMode_keyPressed(app, event):
    app.mode = 'gameMode'


def reset(app, level):
    app.birds = []
    app.pigs = []
    app.boards = []
    app.slingshot = Slingshot(app, app.width // 4)
    app.level = Level(app, app.birds, app.pigs, app.boards)
    app.ground = Ground(app)
    app.level.goToLevel(level)
    app.engine = PhysicsEngine(app.birds, app.pigs, app.boards, app.ground)
    app.score = 0


def gameMode_keyPressed(app, event):
    if event.key in "123":
        reset(app, int(event.key))


def gameMode_mouseDragged(app, event):
    if app.birds:
        app.birds[0].mouseDragged(event)


def gameMode_mouseReleased(app, event):
    if app.birds:
        app.birds[0].mouseReleased(event)


def gameMode_timerFired(app):
    step = 0
    while step < app.steps:

        app.engine.handleCollision()
        for bird in app.birds:
            bird.timerFired()
        for pig in app.pigs:
            pig.timerFired()
        for j in range(len(app.boards)):
            #    print(f"board {j} acc y={app.boards[j].acceleration.y}")
            app.boards[j].timerFired()
            step += 1
    index = 0
    while (index < len(app.birds)):
        bird = app.birds[index]
        if (bird.state == Bird.STATES[4]):
            app.birds.pop(index)
            loadBird(app)
        else:
            index += 1
    index = 0
    while (index < len(app.pigs)):
        if (app.pigs[index].state == Pig.STATES[1]):
            app.pigs.pop(index)
            updateScore(app)
        else:
            index += 1


def updateScore(app):
    app.score = (app.level.pigsCount - len(app.pigs)) * 1000
    if len(app.pigs) == 0:
        if app.level.level < Level.TOTAL_LEVEL:
            reset(app, app.level.level + 1)


def loadBird(app):
    if len(app.birds) > 0:
        app.birds[0].load()


def gameMode_redrawAll(app, canvas):
    app.ground.draw(app, canvas)
    if app.slingshot.state == Slingshot.STATES[0]:
        app.slingshot.draw(app, canvas)
    for bird in app.birds:
        bird.draw(app, canvas)
    if app.slingshot.state == Slingshot.STATES[1]:
        app.slingshot.draw(app, canvas)
    for pig in app.pigs:
        pig.draw(app, canvas)
    for board in app.boards:
        board.draw(app, canvas)

    canvas.create_text(1000, 30, text=f"Level: {app.level.level}", fill="white", font="Consolas 26 bold italic")
    canvas.create_text(1000, 60, text=f"Score: {app.score}", fill="white", font="Consolas 26 bold italic")


def appStarted(app):
    app.mode = 'splashScreenMode'
    app.timerDelay = 200
    app.steps = 10
    reset(app, 1)


runApp(width=1203, height=600)

'''import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d
from ground import *
from ball import *
from level import *
from bird import*
from slingshot import *
from physics_engine import *


#CITATION: I got the splash screen and app mode from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
def splashScreenMode_redrawAll(app, canvas):
    font = 'Consolas 26 bold italic'
    canvas.create_text(app.width/2, 150, text='Welcome to AngryBirds!', font=font, fill="YellowGreen")
    canvas.create_text(app.width/2, 250, text='Press any key to start the game!', font=font, fill="YellowGreen")

def splashScreenMode_keyPressed(app, event):
    app.mode = 'gameMode'

def appStarted(app):
    app.mode = 'splashScreenMode'
    resetApp(app, 1)
    app.timerDelay = 50


def resetApp(app, level):
    app.birds = []
    app.pigs = []
    app.boards = []
    app.ground = Ground(app)
    app.slingshot = Slingshot(app, app.width//4)
    app.level = Level(app, app.birds, app.pigs, app.boards)
    app.level.goToLevel(level)
    app.physicsEngine = PhysicsEngine(app.birds, app.pigs, app.boards, app.ground)
    app.score = 0


def gameMode_keyPressed(app, event):
    if event.key in "123":
        resetApp(app, int(event.key))

def gameMode_mouseDragged(app, event):
    if app.birds:
        app.birds[0].mouseDragged(event)

def gameMode_mouseReleased(app, event):
    if app.birds:
        app.birds[0].mouseReleased(event)


def gameMode_timerFired(app):
    app.physicsEngine.handleCollision()
    for bird in app.birds:
        bird.timerFired()
    for pig in app.pigs:
        pig.timerFired()
    for board in range(len(app.boards)):
        app.boards[board].timerFired()

    i = 0
    while i < len(app.birds):
        bird = app.birds[i]
        if bird.state == Bird.STATES[4]:
            app.birds.pop(i)
        else:
            i += 1

    i = 0
    while i < len(app.pigs):
        if app.pigs[i].state == Pig.STATES[1]:
            app.pigs.pop(i)
            updateScore(app)
        else:
            i += 1

def updateScore(app):
    app.score = (app.level.pigsCount - len(app.pigs)) * 1000
    if len(app.pigs) == 0:
        if app.level.level < Level.TOTAL_LEVEL:
            resetApp(app, app.level.level + 1)

def loadBird(app):
    if len(app.birds) > 0:
        app.birds[0].load()


def gameMode_redrawAll(app, canvas):
    app.ground.draw(app, canvas)
    if app.slingshot.state == Slingshot.STATES[0]:
        app.slingshot.draw(app, canvas)
    for pig in app.pigs:
        pig.draw(app, canvas)
    for bird in app.birds:
        bird.draw(app, canvas)
    if app.slingshot.state == Slingshot.STATES[1]:
        app.slingshot.draw(app, canvas)
    for board in app.boards:
        board.draw(app, canvas)



runApp(width=1440, height=718)

'''