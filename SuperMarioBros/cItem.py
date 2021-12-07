from pico2d import *
import game_framework
import server


PIXEL_PER_METER = (30.0 / 0.3)  # 30 pixel 30 cm
RUN_SPEED_KMPH = 0.5
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Mushroom:
    image = None

    def __init__(self, blockx, blocky):
        if Mushroom.image == None:
            Mushroom.image = load_image('Image/Mushroom.png')
        self.xPos = blockx
        self.yPos = blocky + 15 + 16
        self.type = 1
        self.dir = 1
        self.cx = self.xPos
        self.fall_speed = 0

    def update(self):
        self.xPos += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.cx = self.xPos - server.background.window_left
        self.yPos += -1 * self.fall_speed
        self.fall_speed += 1
        delay(0.01)

    def get_bb(self, bb_type=0):
        w, h = 32, 32
        return self.cx - w / 2, self.yPos - h / 2, self.cx + w / 2, self.yPos + h / 2

    def draw(self):
        self.image.draw(self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Flower:
    image = None

    def __init__(self, blockx, blocky):
        if Flower.image == None:
            Flower.image = load_image('Image/Flower.png')
        self.xPos = blockx
        self.yPos = blocky + 15 + 16
        self.type = 2
        self.cx = self.xPos

    def update(self):
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        w, h = 32, 32
        return self.cx - w / 2, self.yPos - h / 2, self.cx + w / 2, self.yPos + h / 2

    def draw(self):
        self.image.draw(self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

