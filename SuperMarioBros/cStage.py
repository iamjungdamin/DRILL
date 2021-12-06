from pico2d import *
import server


class Background:
    def __init__(self):
        self.image = load_image("Image/Stage2.png")
        self.canvas_width = get_canvas_width()
        self.window_left = 0

    def update(self):
        self.window_left = clamp(0, int(server.mario.xPos) - self.canvas_width // 2, 1986 - self.canvas_width)

    def get_bb(self, bb_type=0):
        # return 0, 0, 0, 0
        pass

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, 0, 800, 600, 0, 0)

    def draw_bb(self):
        # draw_rectangle(*self.get_bb())
        pass


class Flag:
    def __init__(self):
        self.image = load_image("Image/Flag.png")
        self.xPos, self.yPos = 465, 60 + 168

    def update(self):
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        w, h = 5, 336
        return self.cx - w/2, self.yPos - h/2, self.cx + w/2, self.yPos + h/2

    def draw(self):
        self.image.draw(self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Castle:
    def __init__(self):
        self.image = load_image("Image/Castle.png")
        self.xPos, self.yPos = 465 + 180, 60 + 75

    def update(self):
        self.cx = self.xPos - server.background.window_left

    def get_bb(self, bb_type=0):
        w, h = 30, 60
        return self.cx - w/2, self.yPos - 60 - h/2, self.cx + w/2, self.yPos - 60 + h/2

    def draw(self):
        self.image.draw(self.cx, self.yPos)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


def setup():
    server.background = Background()
    server.flag = Flag()
    server.castle = Castle()

