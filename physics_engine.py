from vector import *
from ball import *
from board import *
from bird import *
from pig import *
from ground import *


class PhysicsEngine():
    def __init__(self, birds, pigs, boards, ground):
        self.birds = birds
        self.pigs = pigs
        self.boards = boards
        self.ground = ground

    def handleCollision(self):
        # board and ground

        for i in range(len(self.boards)):
            depth, normal, cp = self.collision_detection(self.boards[i], self.ground)
            if depth != None:
                v = self.boards[i].vertices
                #    for vertex in v:
                #        print(f'vertices={vertex.x},{vertex.y} ')
                self.resolveBoard(self.boards[i], self.ground, normal, depth, cp)

                # bird and pig
        for bird in self.birds:
            for pig in self.pigs:
                if bird.r + pig.r >= (pig.position - bird.position).magnitude():
                    distanceVec = bird.position - pig.position
                    depth = bird.r + pig.r - distanceVec.magnitude()
                    separationVec = distanceVec.unit()
                    bird.position = bird.position + separationVec
                    pig.position = pig.position - separationVec
                    pig.state = Pig.STATES[1]
                    bird.state = Bird.STATES[4]
                    self.resolve(bird, pig)

        # bird and bird
        for bird1 in self.birds:
            for bird2 in self.birds:
                if (bird1 != bird2):
                    if bird1.r + bird2.r >= (bird1.position - bird2.position).magnitude():
                        distanceVec = bird1.position - bird2.position
                        depth = bird1.r + bird2.r - distanceVec.magnitude()
                        separationVec = distanceVec.unit() * (depth / 2)
                        bird1.position = bird1.position + separationVec
                        bird2.position = bird2.position - separationVec
                        self.resolve(bird1, bird2)

        # pig and pig
        for pig1 in self.pigs:
            for pig2 in self.pigs:
                if (pig1 != pig2):
                    if pig1.r + pig2.r >= (pig1.position - pig2.position).magnitude():
                        distanceVec = pig1.position - pig2.position
                        depth = pig1.r + pig2.r - distanceVec.magnitude()
                        separationVec = distanceVec.unit() * (depth / 2)
                        pig1.position = pig1.position + separationVec
                        pig2.position = pig2.position - separationVec

                        self.resolve(pig1, pig2)
        # bird and ground
        for bird in self.birds:
            if bird.position.y < bird.r:
                bird.position.y = bird.r
                bird.velocity.y = bird.velocity.y * (-1) * bird.elasticity
        # pig and ground
        for pig in self.pigs:
            if pig.position.y < pig.r:
                pig.position.y = pig.r
                pig.velocity.y = pig.velocity.y * (-1) * pig.elasticity
        # board and board
        for i in range(len(self.boards)):
            for j in range(len(self.boards)):

                if (self.boards[i] != self.boards[j]):
                    depth, normal, cp = self.collision_detection(self.boards[i], self.boards[j])
                    if depth != None:
                        print(f'board {i},{j} collide depth={depth} cp={cp.x},{cp.y}')
                        self.resolveBoard(self.boards[i], self.boards[j], normal, depth, cp)
        # bird and board
        for i in range(len(self.birds)):
            for j in range(len(self.boards)):
                bird = self.birds[i]
                board = self.boards[j]
                depth, normal, cp = self.collision_detection(bird, board)
                if depth != None:
                    self.boards[j].state = Board.STATES[1]
                    bird.state = Bird.STATES[4]
                    print(f'bird {i},board {j} collide  depth={depth} cp={cp.x},{cp.y}')
                    self.resolveBoard(bird, board, normal, depth, cp)
        # pig and board
        for i in range(len(self.pigs)):
            for j in range(len(self.boards)):
                pig == self.pigs[i]
                board = self.boards[j]
                depth, normal, cp = self.collision_detection(pig, board)
                if depth != None:
                    self.boards[j].state = Board.STATES[1]
                    print(f'pig {i}, board {j} collide')
                    if self.boards[j].velocity.magnitude() > 1:
                        pig.state = Pig.STATES[1]
                    self.resolveBoard(pig, board, normal, depth, cp)
                    # board and pig
        for i in range(len(self.boards)):
            for j in range(len(self.pigs)):
                pig == self.pigs[j]
                board = self.boards[i]
                depth, normal, cp = self.collision_detection(board, pig)
                if depth != None:
                    self.boards[i].state = Board.STATES[1]
                    if self.boards[j].velocity.magnitude() > 1:
                        pig.state = Pig.STATES[1]
                    print(f'board {i}, pig {j} collide')
                    self.resolveBoard(board, pig, normal, depth, cp)

    def getAxes(self, body1, body2):
        axes = []
        if (isinstance(body1, Ball) and isinstance(body2, Ball)):
            axes.append((body2.position - body1.position).unit())
            return axes
        if isinstance(body1, Ball):
            axes.append((self.findClosestVertexToPoint(body1.position, body2.vertices) - body1.position).unit())
        if isinstance(body1, Board):
            axes.append(body1.direction.normal())
            axes.append(body1.direction)
        if isinstance(body2, Ball):
            axes.append((self.findClosestVertexToPoint(body1.position, body2.vertices) - body1.position).unit())
            axes.append((self.findClosestVertexToPoint(body2.position, body1.vertices) - body2.position).unit())
        if isinstance(body2, Board):
            axes.append(body2.direction.normal())
            axes.append(body2.direction)
        if isinstance(body1, Ground):
            axes.append(body1.direction.normal())
        if isinstance(body2, Ground):
            axes.append(body2.direction.normal())
        return axes

    def collision_detection(self, body1, body2):
        minOverlap = None
        overlapAxis = None
        collisionBody = None
        axes = self.getAxes(body1, body2)

        for i in range(len(axes)):
            p1min, p1max, cp = self.projectBodyOnAxis(axes[i], body1)
            p2min, p2max, cp = self.projectBodyOnAxis(axes[i], body2)
            overlap = min(p1max, p2max) - max(p1min, p2min)
            if overlap < 0:
                return None, None, None

            if p1max > p2max and p1min < p2min or \
                    p1max < p2max and p1min > p2min:
                mins = abs(p1min - p2min)
                maxs = abs(p1max - p2max)
                if (mins < maxs):
                    overlap += mins
                else:
                    overlap += maxs
                    axes[i] = axes[i] * (-1)
            if minOverlap == None or overlap < minOverlap:
                minOverlap = overlap
                overlapAxis = axes[i]

                if (i < 1):
                    collisionBody = body2
                    if p1max > p2max:
                        overlapAxis = axes[i] * (-1)
                elif i == 1 and not isinstance(body1, Ball):
                    collisionBody = body2
                    if p1max > p2max:
                        overlapAxis = axes[i] * (-1)
                else:
                    collisionBody = body1
                    if p1max < p2max:
                        overlapAxis = axes[i] * (-1)

        p1min, p1max, cp = self.projectBodyOnAxis(overlapAxis, collisionBody)
        if (collisionBody == body2):
            overlapAxis = overlapAxis * (-1)
        return minOverlap, overlapAxis, cp

    def findBallVertices(self, axis, ball):
        if isinstance(ball, Ball):
            ball.vertices = []
            ball.vertices.append(ball.position - axis.unit() * ball.r)
            ball.vertices.append(ball.position + axis.unit() * ball.r)

    def findClosestVertexToPoint(self, p, vertices):
        minDistance = sys.float_info.max

        for vertex in vertices:
            distance = (p - vertex).magnitude()

            if distance < minDistance:
                minDistance = distance
                result = vertex

        return result

    def projectBodyOnAxis(self, axis, body):
        self.findBallVertices(axis, body)
        min = body.vertices[0].dot(axis)
        max = min
        collisionVertex = body.vertices[0]
        for i in range(len(body.vertices)):

            proj = body.vertices[i].dot(axis)

            if proj < min:
                min = proj
                collisionVertex = body.vertices[i]
            if proj > max:
                max = proj
        return min, max, collisionVertex

    def resolve(self, ball1, ball2):
        collisionNormal = (ball1.position - ball2.position).unit()
        relativeVelocity = ball1.velocity - ball2.velocity
        separationVelocity = relativeVelocity.dot(collisionNormal)
        sepVec1 = - separationVelocity * min(ball1.elasticity, ball2.elasticity)
        ball1.velocity = ball1.velocity + (collisionNormal * sepVec1)
        ball2.velocity = ball2.velocity + (collisionNormal * sepVec1) * (-1)

    def resolveBoard(self, body1, body2, normal, depth, cp):

        rA = cp - body1.position
        vA = body1.velocity + Vector(-body1.angularVelocity * rA.y, body1.angularVelocity * rA.x)
        rB = cp - body2.position
        vB = body2.velocity + Vector(-body2.angularVelocity * rB.y, body2.angularVelocity * rB.x)

        impA = body1.inverse_inertia * (rA.cross(normal)) ** 2
        impB = body2.inverse_inertia * (rB.cross(normal)) ** 2

        vAB = vA - vB
        e = min(body1.elasticity, body2.elasticity)
        impulse = -(1 + e) * (vAB.dot(normal)) / (body1.inverse_mass + body2.inverse_mass + impA + impB)
        impulseVec = normal * impulse

        body1.velocity = body1.velocity + impulseVec * body1.inverse_mass
        body2.velocity = body2.velocity + impulseVec * (-body2.inverse_mass)

        body1.angularVelocity = body1.angularVelocity + body1.inverse_inertia * rA.cross(impulseVec)
        body2.angularVelocity = body2.angularVelocity - body2.inverse_inertia * rB.cross(impulseVec)

        penResolution = normal * (depth / (body1.inverse_mass + body2.inverse_mass))
        body1.position = body1.position + (penResolution * body1.inverse_mass)
        body2.position = body2.position + (penResolution * (-body2.inverse_mass))



'''from rigidbody import *
from cmu_112_graphics import *
from rigidbody import *
from vector import *
from ball import*
from board import*
from pig import*
from bird import*
from ground import*

#current: takes care of collision
class PhysicsEngine():
    def __init__(self, birds, pigs, boards, ground):
        self.birds = birds
        self.pigs = pigs
        self.boards = boards
        self.ground = ground

    def handleCollision(self):
        #1. check if collision occurs between different types of objects
        #2. separates them back from collision state
        #3. determine separation velocity (for final velocity calculation)

        for i in range(len(self.boards)):
            depth, normal, cp = self.collision_detection(self.boards[i], self.ground)
            if depth != None:
                self.resolveBoard(self.boards[i], self.ground, normal, depth, cp)

                # bird and pig
                for bird in self.birds:
                    for pig in self.pigs:
                        if bird.r + pig.r >= (pig.position - bird.position).mag():
                            distanceVec = bird.position - pig.position
                            depth = bird.r + pig.r - distanceVec.mag()
                            separationVec = distanceVec.unit()
                            bird.position = bird.position + separationVec
                            pig.position = pig.position - separationVec
                            pig.state = Pig.STATES[1]
                            bird.state = Bird.STATES[4]
                            self.resolve(bird, pig)

                # bird and bird
                for bird1 in self.birds:
                    for bird2 in self.birds:
                        if (bird1 != bird2):
                            if bird1.r + bird2.r >= (bird1.position - bird2.position).mag():
                                distanceVec = bird1.position - bird2.position
                                depth = bird1.r + bird2.r - distanceVec.mag()
                                separationVec = distanceVec.unit() * (depth / 2)
                                bird1.position = bird1.position + separationVec
                                bird2.position = bird2.position - separationVec
                                self.resolve(bird1, bird2)

                # pig and pig
                for pig1 in self.pigs:
                    for pig2 in self.pigs:
                        if (pig1 != pig2):
                            if pig1.r + pig2.r >= (pig1.position - pig2.position).mag():
                                distanceVec = pig1.position - pig2.position
                                depth = pig1.r + pig2.r - distanceVec.mag()
                                separationVec = distanceVec.unit() * (depth / 2)
                                pig1.position = pig1.position + separationVec
                                pig2.position = pig2.position - separationVec

                                self.resolve(pig1, pig2)

        # board and board
        for i in range(len(self.boards)):
            for j in range(len(self.boards)):
                if (self.boards[i] != self.boards[j]):
                    depth, normal, cp = self.collision_detection(self.boards[i], self.boards[j])
                    if depth != None:
                        self.resolveBoard(self.boards[i], self.boards[j], normal, depth, cp)

        # bird and board
        for i in range(len(self.birds)):
            for j in range(len(self.boards)):
                bird = self.birds[i]
                board = self.boards[j]
                depth, normal, cp = self.collision_detection(bird, board)
                if depth != None:
                    self.boards[j].state = Board.STATES[1]
                    bird.state = Bird.STATES[4]
                    self.resolveBoard(bird, board, normal, depth, cp)
        # pig and board
        for i in range(len(self.pigs)):
            for j in range(len(self.boards)):
                pig == self.pigs[i]
                board = self.boards[j]
                depth, normal, cp = self.collision_detection(pig, board)
                if depth != None:
                    self.boards[j].state = Board.STATES[1]
                    if self.boards[j].velocity.magnitude() > 1:
                        pig.state = Pig.STATES[1]
                    self.resolveBoard(pig, board, normal, depth, cp)
                    # board and pig
        for i in range(len(self.boards)):
            for j in range(len(self.pigs)):
                pig == self.pigs[j]
                board = self.boards[i]
                depth, normal, cp = self.collision_detection(board, pig)
                if depth != None:
                    self.boards[i].state = Board.STATES[1]
                    if self.boards[j].velocity.magnitude() > 1:
                        pig.state = Pig.STATES[1]
                    self.resolveBoard(board, pig, normal, depth, cp)

    # CITATION: the code is based on this video I watched https://youtu.be/RBya4M6SWwk
    # CITATION: I used the separating axis theorem from https://dyn4j.org/2010/01/sat/
    def getAxes(self, body1, body2):
        axes = []
        if (isinstance(body1, Ball) and isinstance(body2, Ball)):
            axes.append((body2.position - body1.position).unit())
            return axes
        if isinstance(body1, Ball):
            axes.append((self.findClosestVertexToPoint(body1.position, body2.vertices) - body1.position).unit())
        if isinstance(body1, Board):
            axes.append(body1.direction.normal())
            axes.append(body1.direction)
        if isinstance(body2, Ball):
            axes.append((self.findClosestVertexToPoint(body1.position, body2.vertices) - body1.position).unit())
            axes.append((self.findClosestVertexToPoint(body2.position, body1.vertices) - body2.position).unit())
        if isinstance(body2, Board):
            axes.append(body2.direction.normal())
            axes.append(body2.direction)
        if isinstance(body1, Ground):
            axes.append(body1.direction.normal())
        if isinstance(body2, Ground):
            axes.append(body2.direction.normal())
        return axes

    def collision_detection(self, body1, body2):
        minOverlap = None
        overlapAxis = None
        collisionBody = None
        axes = self.getAxes(body1, body2)

        for i in range(len(axes)):
            p1min, p1max, cp = self.projectBodyOnAxis(axes[i], body1)
            p2min, p2max, cp = self.projectBodyOnAxis(axes[i], body2)
            overlap = min(p1max, p2max) - max(p1min, p2min)
            if overlap < 0:
                return None, None, None

            if p1max > p2max and p1min < p2min or \
                    p1max < p2max and p1min > p2min:
                mins = abs(p1min - p2min)
                maxs = abs(p1max - p2max)
                if (mins < maxs):
                    overlap += mins
                else:
                    overlap += maxs
                    axes[i] = axes[i] * (-1)
            if minOverlap == None or overlap < minOverlap:
                minOverlap = overlap
                overlapAxis = axes[i]

                if (i < 1):
                    collisionBody = body2
                    if p1max > p2max:
                        overlapAxis = axes[i] * (-1)
                elif i == 1 and not isinstance(body1, Ball):
                    collisionBody = body2
                    if p1max > p2max:
                        overlapAxis = axes[i] * (-1)
                else:
                    collisionBody = body1
                    if p1max < p2max:
                        overlapAxis = axes[i] * (-1)

        p1min, p1max, cp = self.projectBodyOnAxis(overlapAxis, collisionBody)
        if (collisionBody == body2):
            overlapAxis = overlapAxis * (-1)
        return minOverlap, overlapAxis, cp

    def findBallVertices(self, axis, ball):
        if isinstance(ball, Ball):
            ball.vertices = []
            ball.vertices.append(ball.position - axis.unit() * ball.r)
            ball.vertices.append(ball.position + axis.unit() * ball.r)

    def findClosestVertexToPoint(self, p, vertices):
        minDistance = sys.float_info.max

        for vertex in vertices:
            distance = (p - vertex).magnitude()

            if distance < minDistance:
                minDistance = distance
                result = vertex

        return result

    def projectBodyOnAxis(self, axis, body):
        self.findBallVertices(axis, body)
        min = body.vertices[0].dot(axis)
        max = min
        collisionVertex = body.vertices[0]
        for i in range(len(body.vertices)):

            proj = body.vertices[i].dot(axis)

            if proj < min:
                min = proj
                collisionVertex = body.vertices[i]
            if proj > max:
                max = proj
        return min, max, collisionVertex

    #checks if bodies are in collision
    def isInCollision(self, body1, body2):
        if(isinstance(body1, Board) and (isinstance(body2, Board))):
            return False
        if(isinstance(body1, Pig) and (isinstance(body2, Board))):
            return False
        if(isinstance(body1, Bird) and (isinstance(body2, Board))):
            return False

    def resolve(self, ball1, ball2):
        collisionNormal = (ball1.position - ball2.position).unit()
        relativeVelocity = ball1.velocity - ball2.velocity
        separationVelocity = relativeVelocity.dot(collisionNormal)
        sepVec1 = - separationVelocity * min(ball1.elasticity, ball2.elasticity)
        ball1.velocity = ball1.velocity + (collisionNormal * sepVec1)
        ball2.velocity = ball2.velocity + (collisionNormal * sepVec1) * (-1)

    def resolveBoard(self, body1, body2, normal, depth, cp):

        rA = cp - body1.position
        vA = body1.velocity + Vector(-body1.angularVelocity * rA.y, body1.angularVelocity * rA.x)
        rB = cp - body2.position
        vB = body2.velocity + Vector(-body2.angularVelocity * rB.y, body2.angularVelocity * rB.x)

        impA = body1.inverse_inertia * (rA.cross(normal)) ** 2
        impB = body2.inverse_inertia * (rB.cross(normal)) ** 2

        vAB = vA - vB
        e = min(body1.elasticity, body2.elasticity)
        impulse = -(1 + e) * (vAB.dot(normal)) / (body1.inverse_mass + body2.inverse_mass + impA + impB)
        impulseVec = normal * impulse

        body1.velocity = body1.velocity + impulseVec * body1.inverse_mass
        body2.velocity = body2.velocity + impulseVec * (-body2.inverse_mass)

        body1.angularVelocity = body1.angularVelocity + body1.inverse_inertia * rA.cross(impulseVec)
        body2.angularVelocity = body2.angularVelocity - body2.inverse_inertia * rB.cross(impulseVec)

        penResolution = normal * (depth / (body1.inverse_mass + body2.inverse_mass))
        body1.position = body1.position + (penResolution * body1.inverse_mass)
        body2.position = body2.position + (penResolution * (-body2.inverse_mass))



'''