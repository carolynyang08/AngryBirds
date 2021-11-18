from rigidbody import *
from  vector import*

class Board(RigidBody):
    def __init__(self, app, x, y, width, height):
        self.position = Vector(x, y)
        self.width = width
        self.height = height
        self.rotation = 0
        self.verticies = []
        left = -width/2
        right = left + width
        bottom = -height/2
        top = bottom + height
        self.verticies.append(Vector(left, top))
        self.verticies.append(Vector(right, top))
        self.verticies.append(Vector(right, bottom))
        self.verticies.append(Vector(left, bottom))
        self.woodImage1 = app.loadImage('block.png')

    def draw(self, canvas):
        #x, y = convert_coordinates(self.body.position)
        #angle = math.degrees(self.body.angle)
        #self.image = self.image.rotate(angle)
        #canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.image))
        '''offset = Vec2d(*self.image.get_size())/2.
        newposition = Vec2d(x, y) - offset
        canvas.create_image(int(newposition[0]), int(newposition[1]), image=ImageTk.PhotoImage(self.image))'''
