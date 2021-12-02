from pico2d import *
import server


class Stage:
    def __init__(self):
        self.sky = load_image("Image/Stage-sky.png")
        self.canvas_width, self.canvas_height = get_canvas_width(), get_canvas_width()
        self.window_left = 0
        self.xPos, self.yPos = 800 // 2, 600 // 2

    def update(self):
        self.window_left = clamp(0, int(server.mario.xPos) - self.canvas_width // 2, 1986 - self.canvas_width)

    def get_bb(self, bb_type=0):
        return 0, 0, 0, 0

    def draw(self):
        self.sky.clip_draw_to_origin(self.window_left, 0, 800, 600, 0, 0)
        draw_rectangle(*self.get_bb())

