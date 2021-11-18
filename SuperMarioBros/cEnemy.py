from pico2d import *


class Goomba:
    def __init__(self, x=700):
        self.image = load_image('Image/Goomba.png')
        self.xPos = x
        self.yPos = 83 + 16
        self.frame = 0
        self.state = 0  # IDLE, DIED
        self.die_frame = 0.0
        self.type = 'enemy'

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.xPos -= 0.05

        if self.state == 1:
            self.die_frame += 0.01

    def get_bb(self):
        w, h = 32, 32
        return self.xPos - w / 2, self.yPos - h / 2, self.xPos + w / 2, self.yPos + h / 2

    def draw(self):
        if self.state == 0:
            self.image.clip_draw(self.frame * 59, 0, 32, 32, self.xPos, self.yPos)
        elif self.state == 1:
            self.image.clip_draw(2 * 59, 0, 32, 32, self.xPos, self.yPos)
        draw_rectangle(*self.get_bb())


class Turtle:
    def __init__(self, x=700):
        self.image = load_image('Image/Turtle.png')
        self.xPos = x
        self.yPos = 83 + 24
        self.frame = 0
        self.state = 0  # IDLE, DIED
        # TODO: DIED sprite
        self.die_frame = 0.0
        self.type = 'enemy'

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.xPos -= 0.05

        if self.state == 1:
            self.die_frame += 0.01

    def get_bb(self):
        w, h = 32, 48
        return self.xPos - w / 2, self.yPos - h / 2, self.xPos + w / 2, self.yPos + h / 2

    def draw(self):
        if self.state == 0:
            self.image.clip_draw(self.frame * 59, 0, 32, 48, self.xPos, self.yPos)
        elif self.state == 1:
            self.image.clip_draw(2 * 59, 0, 32, 48, self.xPos, self.yPos)
        draw_rectangle(*self.get_bb())