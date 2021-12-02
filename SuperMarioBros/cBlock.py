from pico2d import *
import game_framework


TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3


class ItemBlock:
    image = None

    def __init__(self, x, y):
        if ItemBlock.image == None:
            ItemBlock.image = load_image('Image/itemblock.png')
        self.xPos = x
        self.yPos = y
        self.frame = 0

    def update(self):
        if not self.frame == 3:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def get_bb(self, bb_type=0):
        # 0 ground, 1 block
        w, h = 30, 30
        if bb_type == 0:
            return self.xPos - w / 2, self.yPos, self.xPos + w / 2, self.yPos + h / 2
        elif bb_type == 1:
            return self.xPos - w / 2, self.yPos - h / 2, self.xPos + w / 2, self.yPos

    def draw(self):
        self.image.clip_draw(int(self.frame) * 56, 0, 30, 30, self.xPos, self.yPos)
        draw_rectangle(*self.get_bb(0))
        draw_rectangle(*self.get_bb(1))


class BrickBlock:
    image = None

    def __init__(self, x, y):
        if BrickBlock.image == None:
            BrickBlock.image = load_image('Image/Brickblock.png')
        self.xPos = x
        self.yPos = y
        self.frame = 0

    def update(self):
        pass

    def get_bb(self, bb_type=0):
        w, h = 30, 30
        if bb_type == 0:
            return self.xPos - w / 2, self.yPos, self.xPos + w / 2, self.yPos + h / 2
        elif bb_type == 1:
            return self.xPos - w / 2, self.yPos - h / 2, self.xPos + w / 2, self.yPos

    def draw(self):
        self.image.draw(self.xPos, self.yPos)
        draw_rectangle(*self.get_bb(0))
        draw_rectangle(*self.get_bb(1))


