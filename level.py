import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d
from bird import *

class Level():
    def __init__(self, birds, pigs, boards, ground, slingshot):
        self.birds = birds
        self.pigs = pigs
        self.boards = boards
        self.ground = ground
        self.slingshot = slingshot

    def gotToLevel(self, level):

    def levelOne(self, app):
        bird = Bird(self.app.width/4 -12, self.app)


