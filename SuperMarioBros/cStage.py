from pico2d import *
import server


class Stage:
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

