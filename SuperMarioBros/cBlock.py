from pico2d import *


class Block:
    def __init__(self, x, y):
        self.image = load_image('Image/itemblock.png')
        self.xPos = x
        self.yPos = y
        self.type = 'block'

    def update(self):
        pass

    def get_bb(self):
        w, h = 160, 160  # TODO: size
        # TODO: 윗부분은 ground 아랫부분은 block
        return self.xPos - w / 2, self.yPos - h / 2, self.xPos + w / 2, self.yPos + h / 2

    def draw(self):
        self.image.draw(self.xPos, self.yPos)
