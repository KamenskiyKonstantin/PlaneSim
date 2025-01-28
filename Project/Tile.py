from pygame import Surface, image

TILE_SIZE = 50

class Tile:
    def __init__(self, x: int, y: int, size: int, type: str):
        self.x = x
        self.y = y
        self.size = size
        self.type = type
        self.image = image.load(f"static/{type}.png")

    def draw(self, surface: Surface):
        surface.blit(self.image, (self.x*TILE_SIZE, self.y*TILE_SIZE))

