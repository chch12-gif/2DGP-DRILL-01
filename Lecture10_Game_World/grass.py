from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x= 400
        self.y= 30

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
