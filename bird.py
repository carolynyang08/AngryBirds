from ball import *
import math
from cmu_112_graphics import *
from vector import*
from slingshot import *
from PIL import Image


class Bird(Ball):
    MAX_SPEED = 100
    STATES = ['resting', 'loaded', 'aiming', 'launched', 'dead']
    def __init__(self, app, x, y, r, mass, state):
        super().__init__(app, x, y, r, mass)
        self.loadedPosition = Vector(self.position.x, self.position.y)
        self.state = state
        self.birdImage = app.loadImage('resources/images/red-bird2.png')
        self.loadedPosition = Vector(app.slingshot.centerx, app.slingshot.centery)


    def isInCircle(self, x, y):
        if math.sqrt((x-self.position.x)**2 +
                     (y-self.position.y)**2) <= self.r:
            return True
        else:
            return False

    def load(self):
        self.state = self.STATES[1]
        self.position = Vector(self.loadedPosition.x, self.loadedPosition.y)

    def mouseDragged(self, event):
        x, y = RigidBody.convert_coordinates((event.x, event.y), self.app.height)
        if self.state == Bird.STATES[1] and self.isInCircle(x, y):
            self.state = Bird.STATES[2]

        elif self.state == Bird.STATES[2]:

            self.position.x, self.position.y = x, y
            pullVec = self.position - self.loadedPosition
            pullMag = pullVec.magnitude()
            if pullMag > Slingshot.MAX:
                pullVec = pullVec.unit() * Slingshot.MAX
                self.position = self.loadedPosition + pullVec
            self.app.slingshot.mouseDragged(self.app.birds[0])
            self.velocity = pullVec/Slingshot.MAX * (-1) * Bird.MAX_SPEED
            self.acceleration = Vector(0, RigidBody.GRAVITY)



    def timerFired(self):
        if self.position.y > self.r:
            self.acceleration.y = RigidBody.GRAVITY
        else:
            self.acceleration.y = RigidBody.GRAVITY
        if self.state == Bird.STATES[3]:
            self.move()


    def mouseReleased(self, event):
        if self.state == Bird.STATES[2]:
            self.state = Bird.STATES[3]
            self.app.slingshot.mouseReleased(event)


    def draw(self, app, canvas):
        x, y = RigidBody.convert_coordinates((self.position.x, self.position.y), app.height)

        canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.birdImage))
        canvas.create_oval(x - self.r, y - self.r, x + self.r, y + self.r,
                           width=1, outline="black")

        if self.state == Bird.STATES[2]:
            self.drawPredTraj(app, canvas)

    def drawPredTraj(self, app, canvas):
        circleRadius = 3
        time = (app.width) / max(1, self.velocity.x)
        for i in range(1, int(time)):
            x = self.position.x + self.velocity.x * i
            y = self.position.y + self.velocity.y * i + .5 * RigidBody.GRAVITY * i ** 2
            plotx, ploty = RigidBody.convert_coordinates((x, y), app.height)
            canvas.create_oval(plotx - circleRadius, ploty - circleRadius, \
                          plotx + circleRadius, ploty + circleRadius, fill="white")


