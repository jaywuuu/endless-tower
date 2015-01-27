# constants, don't change!
OBJCLASS_PLAYER     = 0
OBJCLASS_MONSTER    = 1
OBJCLASS_ITEM       = 2

class Object:
    def __init__(self, x, y, symbol, objClass):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.objClass = objClass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
