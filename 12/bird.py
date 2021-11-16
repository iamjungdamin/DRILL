import random
from pico2d import *
import game_world
import game_framework


# 새의 크기는 100*100픽셀이고, 1픽셀은 3cm입니다. 새의 속도는 50km/h입니다.
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y = random.randint(0, 1600-1), random.randint(400, 500)
        self.dir = random.randint(-1, 1)
        if self.dir == 0:
            self.dir = 1
        self.velocity = self.dir * RUN_SPEED_PPS
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        if self.x < 25 or self.x > 1600 - 25:
            self.dir *= -1
            self.velocity = self.dir * RUN_SPEED_PPS

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)



