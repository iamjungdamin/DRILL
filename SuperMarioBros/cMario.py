from pico2d import *


class Mario:
    def __init__(self):
        self.image = [
            load_image('Image/SmallMario.png'), load_image('Image/BigMario.png'), load_image('Image/FireMario.png')
        ]
        self.xPos = 100
        self.yPos = 83 + 32
        self.frame = 0
        # TODO: enum으로 관리
        self.trans = 0  # SMALL, BIG, FIRE
        self.state = 0  # IDLE, LEFT, RIGHT, JUMP, ATTACK

    def update(self):
        # TODO: Animation
        # self.frame = (self.frame + 1) % 4

        events = get_events()
        for e in events:
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_LEFT:
                    self.xPos -= 5
                elif e.key == SDLK_RIGHT:
                    self.xPos += 5
                # trans 확인용
                elif e.key == SDLK_0:
                    self.trans = 0
                elif e.key == SDLK_1:
                    self.trans = 1
                elif e.key == SDLK_2:
                    self.trans = 2

    def draw(self):
        self.image[self.trans].clip_draw(405, 0, 58, 64, self.xPos, self.yPos)

