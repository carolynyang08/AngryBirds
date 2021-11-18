import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d
from bird import *
from pig import *

class Level():
    def __init__(self, app, birds, pigs, boards, ground, slingshot):
        self.birds = birds
        self.pigs = pigs
        self.boards = boards
        self.ground = ground
        self.slingshot = slingshot
        self.app = app

    def goToLevel(self, level):
        if level == 1:
            self.level1()

    def level1(self):
        for i in range(3):
            if i == 0:
                bird = Bird(self.app, self.app.width // 4 - 12, \
                            self.app.slingshot.imageHeight - 35, 17,\
                            Bird.STATES[1])
            else:
                bird = Bird(self.app, self.app.width//4 - 12 -\
                            (i * 4 * bird.r), 17, 17, Bird.STATES[0])
            self.birds.append(bird)
        for i in range(3):
            pig = Pig(self.app, self.app.width//4 * 3 + (i) * 60, 30, 20)
            self.pigs.append(pig)





