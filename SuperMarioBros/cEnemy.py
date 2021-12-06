from pico2d import *
import game_framework
import server
from random import randint


PIXEL_PER_METER = (30.0 / 0.3)  # 30 pixel 30 cm
RUN_SPEED_KMPH = 0.5
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2


class Goomba:
    image = None

    def __init__(self, x, y=60+16):
        if Goomba.image == None:
            Goomba.image = load_image('Image/Goomba.png')
        self.xPos = x
        self.yPos = y
        self.frame = 0
        self.dir = -1
        self.state = 0  # IDLE, DIED
        self.die_frame = 0.0

    def update(self):
        if self.state == 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            self.xPos += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.die_frame += game_framework.frame_time
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        w, h = 32, 32
        return self.cx - w / 2, self.yPos - h / 2, self.cx + w / 2, self.yPos + h / 2

    def draw(self):
        if self.state == 0:
            self.image.clip_draw(int(self.frame) * 59, 0, 32, 32, self.cx, self.yPos)
        else:
            self.image.clip_draw(2 * 59, 0, 32, 32, self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Turtle:
    image = None

    def __init__(self, x, y=60+24):
        if Turtle.image == None:
            Turtle.image = load_image('Image/Turtle.png')
        self.xPos = x
        self.yPos = y
        self.frame = 0
        self.dir = -1
        self.state = 0  # IDLE, DIED
        self.die_frame = 0.0

    def update(self):
        if self.state == 0:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            self.xPos += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.die_frame += game_framework.frame_time
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        w, h = 32, 48
        return self.cx - w / 2, self.yPos - h / 2, self.cx + w / 2, self.yPos + h / 2

    def draw(self):
        if self.state == 0:
            if self.dir == -1:
                self.image.clip_draw(int(self.frame) * 59, 0, 32, 48, self.cx, self.yPos)
            else:
                self.image.clip_composite_draw(int(self.frame) * 59, 0, 32, 48, 0, 'h', self.cx, self.yPos, 32, 48)
        else:
            self.image.clip_draw(2 * 59, 0, 32, 48, self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


def setup():
    server.enemies = [Goomba(16 + 32 * 15)]
    server.enemies += [Turtle(16 + 32 * 18)]
