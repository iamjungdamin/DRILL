from pico2d import *


class Goomba:
    def __init__(self, x=700):
        self.image = load_image('Image/Goomba.png')
        self.xPos = x
        self.yPos = 83 + 16
        self.frame = 0
        self.state = 0  # IDLE, DIED

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.xPos -= 0.05

    def get_bb(self):
        w, h = 32, 32
        return self.xPos - w / 2, self.yPos - h / 2, self.xPos + w / 2, self.yPos + h / 2

    def draw(self):
        if self.state == 0:
            self.image.clip_draw(self.frame * 59, 0, 32, 32, self.xPos, self.yPos)
        # TODO: 밟힌 모습 1초간 draw

