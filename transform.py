from vector import*

class Transformer():
    def __init__(self, position, angle):
        self.position = position
        self.angle = angle
        self.sin = math.sin(angle)
        self.cos = math.cos(angle)