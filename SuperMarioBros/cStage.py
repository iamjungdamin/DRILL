from pico2d import *


class Stage:
    def __init__(self):
        self.sky = load_image("Image/Stage-sky.png")
        self.ground = load_image("Image/Stage-ground.png")
        self.xPos, self.yPos = 800 // 2, 600 // 2

    def get_bb(self):
        w, h = 1986, 600
        return self.xPos - w//2, self.yPos - h//2, self.xPos + w//2, self.yPos - h//2 + 83

    def draw(self):
        self.sky.draw(self.xPos, self.yPos)
        self.ground.draw(self.xPos, self.yPos)

