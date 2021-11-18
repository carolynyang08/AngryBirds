from rigidbody import *
from cmu_112_graphics import *
from rigidbody import *
from vector import *
from ball import*

class PhysicsEngine():
    def __init__(self, birds, pigs, boards, ground):
        self.birds = birds
        self.pigs = pigs
        self.boards = boards
        self.ground = ground

    def handleCollision(self):
        #1. check if collision
        #2. separate them back
        #3. find separation velocity

        for bird in self.birds:
            for pig in self.pigs:
                radSum = bird.r + pig.r
                apartVec = bird.position - pig.position
                apartMag = apartVec.magnitude()
                if apartMag <= radSum:
                    penDepth = radSum - apartMag
                    sepVec = apartVec.unit() * penDepth * .5
                    bird.position = bird.position + sepVec
                    pig.position = pig.position - sepVec
                    self.resolve(bird, pig)

        for bird1 in self.birds:
            for bird2 in self.birds:
                if bird1 != bird2:
                    radSum = bird1.r + bird2.r
                    apartVec = bird1.position -  bird2.position
                    apartMag = apartVec.magnitude()
                    if apartMag <= radSum:
                        penDepth = radSum - apartMag
                        sepVec = apartVec.unit() * penDepth * .5
                        bird1.position = bird1.position + sepVec
                        bird2.position = bird2.position - sepVec
                        self.resolve(bird1, bird2)

        for pig1 in self.pigs:
            for pig2 in self.pigs:
                if pig1 != pig2:
                    radSum = pig1.r + pig2.r
                    apartVec = pig1.position -  pig2.position
                    apartMag = apartVec.magnitude()
                    if apartMag <= radSum:
                        penDepth = radSum - apartMag
                        sepVec = apartVec.unit() * penDepth * .5
                        pig1.position = pig1.position + sepVec
                        pig2.position = pig2.position - sepVec
                        self.resolve(pig1, pig2)

        for bird in self.birds:
            if bird.position.y < bird.r:
                bird.position.y = bird.r
                bird.velocity.y = - bird.velocity.y * Ball.ELASTICITY

        for pig in self.pigs:
            if pig.position.y < pig.r:
                pig.position.y = pig.r
                pig.velocity.y = - pig.velocity.y * Ball.ELASTICITY


    def resolve(self, body1, body2):
        #conservation of mommentum : m1u1 + m2u2 = m1V1 + m2V2
        #conservation of energy: .5 * m1u1^2 + .5 * m2u2^2 = .5 * m1v1^2 + .5 * m2v2^2
        if isinstance(body1, Ball) and isinstance(body2, Ball):
            relativeVelocity = body1.velocity - body2.velocity
            collisionNormal = (body1.position - body2.position).unit()
            sepVelocity = relativeVelocity.dot(collisionNormal)
            sepVelAfterElast = -sepVelocity * Ball.ELASTICITY
            body1.velocity = body1.velocity + collisionNormal * sepVelAfterElast
            body2.velocity = body2.velocity - collisionNormal * sepVelAfterElast










