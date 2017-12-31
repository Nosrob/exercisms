import operator

EAST = {"advance":(1,0)}
NORTH = {"advance":(0,1)}
WEST = {"advance":(-1,0)}
SOUTH = {"advance":(0,-1)}

NORTH["left"] = WEST
SOUTH["left"] = EAST
EAST["left"] = NORTH
WEST["left"] = SOUTH

NORTH["right"] = EAST
SOUTH["right"] = WEST
EAST["right"] = SOUTH
WEST["right"] = NORTH

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing=bearing
        self.coordinates=(x,y)

    def advance(self):
        self.coordinates = tuple(map(operator.add, self.bearing["advance"], self.coordinates))

    def turn_right(self):
        self.bearing = self.bearing["right"]

    def turn_left(self):
        self.bearing = self.bearing["left"]

    def simulate(self, path):
        for x in path:
            if x == 'L': self.turn_left()
            elif x == 'R': self.turn_right()
            elif x == 'A': self.advance()
