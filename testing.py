import pymunk
from cmu_112_graphics import *
from pymunk.vec2d import Vec2d


ball_radius = 30


class Ball():
    def __init__(self, app):
        self.body = pymunk.Body()
        self.body.position = 400, 800
        self.shape = pymunk.Circle(self.body, ball_radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        app.space.add(self.body, self.shape)
        self.image1 = app.scaleImage(app.image, 2 * (ball_radius / app.image.size[0]))

    def draw(self, canvas):
        x, y = convert_coordinates(self.body.position)
        canvas.create_image(int(x), int(y), image=ImageTk.PhotoImage(self.image1))
        # canvas.create_oval(int(x - app.ball_radius), int(y - app.ball_radius),
        # int(x + app.ball_radius), int(y + app.ball_radius), fill="yellow")

class Floor():
    def __init__(self, app):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, (0, 250), (800, 50), 5)
        self.shape.elasticity = 1
        app.space.add(self.body, self.shape)
    def draw(self, canvas):
        canvas.create_line(0, 550, 800, 750, fill="black", width=5)


def appStarted(app):
    app.space = pymunk.Space()
    app.timerDelay = 20
    app.FPS = 1000/app.timerDelay
    app.space.gravity = 0, -1000

    url = 'https://lh3.googleusercontent.com/proxy/l6RDfTseI' \
          '_55Y4A9yv03KFORl9DQlUVx3T8vbk5yhwB6V6-G26IiN-LYhoXIfF' \
          '0OhreD2owU4CPInQl3OdeOiN1-'
    app.image = app.loadImage(url)
    app.ball = Ball(app)
    app.ball2 = Ball(app)
    app.ball3 = Ball(app)
    app.ball4 = Ball(app)
    app.ball5 = Ball(app)
    app.floor = Floor(app)




def keyPressed(app, event):
    pass



def timerFired(app):
    app.space.step(1/app.FPS)

def convert_coordinates(point):
    return point[0], 800 - point[1]


def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, 800, 800, fill="white")
    app.ball.draw(canvas)
    app.ball2.draw(canvas)
    app.ball3.draw(canvas)
    app.ball4.draw(canvas)
    app.ball5.draw(canvas)
    app.floor.draw(canvas)


    #canvas.create_line(cx - 400, cy, cx + 400, cy, fill="black", width=3)'''





def playAngryBirds():
    runApp(width=800, height=800)




def main():
    playAngryBirds()


main()
