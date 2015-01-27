MAP_WIDTH = 80
MAP_HEIGHT = 45

tilemap = []

class Tile:
    def __init__(self, symbol, blocked, visible):
        self.symbol = symbol
        self.blocked = blocked
        self.visible = visible

def init_map(width, height):
    MAP_WIDTH = width
    MAP_HEIGHT = height
    tilemap = [[0 for x in range(MAP_WIDTH)] for x in range(MAP_HEIGHT)]

class Map:
    pass

