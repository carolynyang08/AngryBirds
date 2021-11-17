class RigidBody():
    GRAVITY = -9.8



    @staticmethod
    def convert_coordinates(point, screenHeight):
        return point[0], screenHeight - point[1]


