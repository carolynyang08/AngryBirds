from rigidbody import *
from rotationMatrix import*
from vector import*

class Board(RigidBody):
    STATES = ["passive", "active"]
    def __init__(self, app, x, y, width, height):
        super().__init__(x, y, 0)

        self.app = app
        self.width = width
        self.height = height

        self.left = -self.width / 2
        self.right = self.left + self.width
        self.bottom = -self.height / 2
        self.top = self.bottom + self.height

        self.initialHeight = self.position.y
        self.state = Board.STATES[0]
        self.vertices = []

        self.vertices.append(Vector(self.left, self.top) + self.position)
        self.vertices.append(Vector(self.right, self.top) + self.position)
        self.vertices.append(Vector(self.right, self.bottom) + self.position)
        self.vertices.append(Vector(self.left, self.bottom) + self.position)


        self.orientation = (self.vertices[1] - self.vertices[0]).unit()
        self.initialOrientation = (self.vertices[1] - self.vertices[0]).unit()

        self.mass = 50
        if self.mass == 0:
            self.inverse_mass = 0
        else:
            self.inverse_mass = 1 / self.mass
        self.inertia = self.mass * ((self.width / RigidBody.PIXELS_PER_METER) ** 2 \
                                            + (self.height / RigidBody.PIXELS_PER_METER) ** 2) / 12
        if self.inertia == 0:
            self.inverse_inertia = 0
        else:
            self.inverse_inertia = 1 / self.inertia

    def draw(self, app, canvas):
        x1, y1 = RigidBody.convert_coordinates((self.vertices[0].x, self.vertices[0].y), app.height)
        x2, y2 = RigidBody.convert_coordinates((self.vertices[1].x, self.vertices[1].y), app.height)
        x3, y3 = RigidBody.convert_coordinates((self.vertices[2].x, self.vertices[2].y), app.height)
        x4, y4 = RigidBody.convert_coordinates((self.vertices[3].x, self.vertices[3].y), app.height)

        canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill="brown")

    def move(self):

        self.velocity = (self.velocity + self.acceleration) * (1.0 - self.friction)
        self.position = (self.position * RigidBody.PIXELS_PER_METER + self.velocity )/RigidBody.PIXELS_PER_METER
        self.angle = self.angle + self.angularVelocity

        matrix = RotationMatrix(self.angle)
        self.direction = matrix.multiply(self.initialDirection)
        self.vertices[0] = self.position + self.direction * (-self.width/2) + self.direction.normal() * self.height/2
        self.vertices[1] = self.position + self.direction * ( self.width/2) + self.direction.normal() * self.height/2
        self.vertices[2] = self.position + self.direction * (self.width/2) - self.direction.normal() * self.height/2
        self.vertices[3] = self.position + self.direction * (self.width/2) + self.direction.normal() * self.height/2

    def timerFired(self):
        if self.isBalanced() or self.position.y <= min(self.height, self.width):
            self.acceleration.y = 0
        else:
            self.acceleration.y = RigidBody.GRAVITY
        self.move()

    def isBalanced(self):
        lowestY = self.vertices[0].y
        lowestIndex = 0

        for i in range(1,4):
            if self.vertices[i].y < lowestY:
                lowestY = self.vertices[i].y
                lowestIndex = i
        restList = []
        for i in range(4):
            if i != lowestIndex:
                restList.append(self.vertices[i])
        secondLowestY = restList[0].y
        secondLowestIndex = 0
        for i in range(3):
            if restList[i].y < secondLowestY:
                secondLowestY = self.vertices[i].y
                secondLowestIndex = i
        p1 = self.vertices[lowestIndex]
        p2 = restList[secondLowestIndex]
        if p1.y < 2 and p2.y < 2:
            return True
        if (p1 -p2).magnitude() > min(self.width, self.height):
            if self.findSupport(p1) and self.findSUpport(p2):
                return True
            else:
                return False
        else:
            if self.findSupport(p1) or self.findSupport(p2):
                return True
            else:
                return False

    def findSupport(self, vertex):
        i = 0
        while i < len(self.app.boards):
            other = self.app.boards[i]
            if other != self:
                for j in range(4):
                    if (vertex - other.vertices[j]).magnitude() < 0.01 * min(self.width, self.height):
                        return True
            i += 1
        #return False


