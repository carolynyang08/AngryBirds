from rigidbody import *
class Board(RigidBody):

    class Wood():
        def __init__(self, app, x, y, length, height, image):
            self.body = pymunk.Body(7, 10000)
            self.body.position = x, y
            self.shape = pymunk.Poly.create_box(self.body, (length, height))
            self.shape.density = 1
            self.shape.elasticity = 0.8
            self.shape.friction = 0.8
            self.shape.collision_type = 1
            app.space.add(self.body, self.shape)
            self.image = image
            # self.image1 = app.scaleImage(image, .25)
            # app.bird.sprites = []

        def draw(self, canvas):
            x, y = convert_coordinates(self.body.position)
            angle = math.degrees(self.body.angle)
            self.image = self.image.rotate(angle)
            canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.image))
            '''offset = Vec2d(*self.image.get_size())/2.
            newposition = Vec2d(x, y) - offset
            canvas.create_image(int(newposition[0]), int(newposition[1]), image=ImageTk.PhotoImage(self.image))'''
    pass