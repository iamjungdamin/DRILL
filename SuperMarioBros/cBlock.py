from pico2d import *
import game_framework
import server


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
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        # 0 ground, 1 block
        w, h = 30, 30
        if bb_type == 0:
            return self.cx - w / 2, self.yPos, self.cx + w / 2, self.yPos + h / 2
        elif bb_type == 1:
            return self.cx - w / 2, self.yPos - h / 2, self.cx + w / 2, self.yPos

    def draw(self):
        self.image.clip_draw(int(self.frame) * 56, 0, 30, 30, self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb(0))
        draw_rectangle(*self.get_bb(1))


class BrickBlock:
    image = None

    def __init__(self, x, y):
        if BrickBlock.image == None:
            BrickBlock.image = load_image('Image/brickblock.png')
        self.xPos = x
        self.yPos = y
        self.frame = 0

    def update(self):
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        w, h = 30, 30
        if bb_type == 0:
            return self.cx - w / 2, self.yPos, self.cx + w / 2, self.yPos + h / 2
        elif bb_type == 1:
            return self.cx - w / 2, self.yPos - h / 2, self.cx + w / 2, self.yPos

    def draw(self):
        self.image.draw(self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb(0))
        draw_rectangle(*self.get_bb(1))


class FloorBlock:
    image = None

    def __init__(self, x, y):
        if FloorBlock.image == None:
            FloorBlock.image = load_image('Image/floorblock.png')
        self.xPos = x
        self.yPos = y
        self.frame = 0

    def update(self):
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        w, h = 30, 30
        return self.cx - w / 2, self.yPos - h / 2, self.cx + w / 2, self.yPos + h / 2

    def draw(self):
        self.image.draw(self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


def setup():
    server.itemBlocks = [ItemBlock(15 + 30 * 10, 15 + 30 * 6),
                         ItemBlock(15 + 30 * 15, 15 + 30 * 6),
                         ItemBlock(15 + 30 * 16, 15 + 30 * 10),
                         ItemBlock(15 + 30 * 17, 15 + 30 * 6)]
    server.brickBlocks = [BrickBlock(15 + 30 * 14, 15 + 30 * 6),
                          BrickBlock(15 + 30 * 16, 15 + 30 * 6),
                          BrickBlock(15 + 30 * 18, 15 + 30 * 6)]
    server.floorBlocks = [FloorBlock(15 + 30 * i, 15) for i in range(66)] + \
                         [FloorBlock(15 + 30 * i, 45) for i in range(66)]

