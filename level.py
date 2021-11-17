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
        bird = Bird(self.app.width/4 - 12, self.app.slingshot.imageHeight - 35, 17, self.app)
        self.birds.append(bird)
        pig = Pig(self.app.width//4 * 3, 30, 20, self.app)
        self.pigs.append(pig)




