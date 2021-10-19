from pico2d import *


class Goomba:
    def __init__(self):
        self.image = load_image('Image/Goomba.png')
        self.xPos = 700
        self.yPos = 83 + 20
        self.frame = 0
        self.state = 0  # IDLE, DIED

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.xPos -= 0.05

    def draw(self):
        self.image.clip_draw(self.frame * 59, 0, 31, 32, self.xPos, self.yPos)


