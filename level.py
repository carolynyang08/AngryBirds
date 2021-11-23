import math
from cmu_112_graphics import *
from PIL import Image
from pymunk.vec2d import Vec2d
from bird import *
from pig import *
from board import *
from slingshot import *
from ground import *

class Level():
    TOATAL_LEVEL = 3
    def __init__(self, app, birds, pigs, boards):
        self.birds = birds
        self.pigs = pigs
        self.boards = boards
        self.app = app
        self.level = 1
        self.birdsCount = len(self.birds)
        self.pigsCount = len(self.pigs)

    def goToLevel(self, level):
        if level == 1:
            self.level1()

    def level1(self):
        self.pigsCount = 3
        for i in range(3):
            if i == 0:
                bird = Bird(self.app, self.app.width // 4 - 12, \
                            self.app.slingshot.imageHeight - 35, 17,\
                            1, Bird.STATES[1])
            else:
                bird = Bird(self.app, self.app.width//4 - 12 -\
                            (i * 4 * bird.r), 17, 17, 1, Bird.STATES[0])
            self.birds.append(bird)

        board = Board(self.app, self.app.width // 4 * 3, 25, 10, 50)
        #self.boards.append(board)

        for i in range(3):
            pig = Pig(self.app, self.app.width//4 * 3 + board.width * 2 + i * 60, 30, 20, 10)
            self.pigs.append(pig)

        def level2(self):
            self.pigsCount = 1
            for i in range(2):
                board = Board(self.app, self.width//4 * 3 + i * 50, 30, 10, 60)
                self.boards.append(board)
            board = Board(self.app, self.width//4 * 3 + 25, 65, 60, 10)
            self.boards.append(board)
            for i in range(3):
                if i == 0:
                    bird = Bird(self.app, self.app.slingshot.centerx, self.app.slingshot.centery, 10, 1, Bird.STATES[1])
                else:
                    bird = Bird(self.app, self.app.width//4 - 12 - i * 2 * (10 + 5), 10, 10, 1, Bird.STATES[0])
                self.birds.append(bird)
            for i in range(1):
                pig = Pig(self.app, self.width//4 * 3 + 25, 30 + 62*i, 20, 10)
                self.pigs.append(pig)

        def level3(self):
            self.pigsCount = 2
            for i in range(2):
                board = Board(self.app, self.width//4 * 3 + i * 50, 30, 10, 60)
                self.boards.append(board)
            board = Board(self.app, self.width//4 * 3 + 25, 65, 60, 10)
            self.boards.append(board)
            for i in range(2):
                board = Board(self.app, self.width//4 * 3 + i * 50, 100, 10, 60)
                self.boards.append(board)
            board = Board(self.app, self.width//4 * 3 + 25, 135, 60, 10)
            self.boards.append(board)
            for i in range(3):
                if i == 0:
                    bird = Bird(self.app, self.app.slingshot.centerx, self.app.slingshot.centery, 10, 1, Bird.STATES[1])
                else:
                    bird = Bird(self.app, self.app.width//4 - 12 - i * 2 * (10 + 5), 10, 10, 1, Bird.STATES[0])
                self.birds.append(bird)
            for i in range(2):
                pig = Pig(self.app, self.width//4 * 3 + 25, 30 + 62*i, 20, 10)
                self.pigs.append(pig)












