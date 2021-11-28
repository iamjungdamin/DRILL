from pico2d import *
import server


class Stage:
    def __init__(self):
        self.sky = load_image("Image/Stage-sky.png")
        self.ground = load_image("Image/Stage-ground.png")
        self.xPos, self.yPos = 800 // 2, 600 // 2

    def update(self):
        pass

    def get_bb(self, bb_type=0):
        w, h = 1986, 600
        return self.xPos - w//2, self.yPos - h//2, self.xPos + w//2, self.yPos - h//2 + 83

    def draw(self):
        # self.sky.draw(self.xPos, self.yPos)
        left = clamp(0, int(server.mario.xPos) - 800 // 2, 1986 - 800)
        self.sky.clip_draw(left, 0, 800, 600, self.xPos, self.yPos)
        self.ground.draw(self.xPos, self.yPos)
        draw_rectangle(*self.get_bb())

