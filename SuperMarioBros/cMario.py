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
        self.state = 0  # LEFT, IDLE, RIGHT, JUMP, ATTACK

    def input(self, events):
        for e in events:
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_LEFT:
                    self.state -= 1
                elif e.key == SDLK_RIGHT:
                    self.state += 1

                # TODO: 변신 아이템, 몬스터와 충돌 시 변신
                elif e.key == SDLK_0:
                    self.trans = 0
                elif e.key == SDLK_1:
                    self.trans = 1
                elif e.key == SDLK_2:
                    self.trans = 2

            if e.type == SDL_KEYUP:
                if e.key == SDLK_LEFT:
                    self.state += 1
                elif e.key == SDLK_RIGHT:
                    self.state -= 1

    def update(self):
        if self.state == 0:
            self.frame = 0
        else:
            self.frame = (self.frame + 1) % 4
            # TODO: 왼쪽

        if -1 <= self.state <= 1:
            self.xPos += self.state

    def draw(self):
        if self.trans == 2:
            self.image[self.trans].clip_draw(416 + self.frame * 56, 0, 32, 64, self.xPos, self.yPos)
        else:
            self.image[self.trans].clip_draw(416 + self.frame * 60, 0, 32, 64, self.xPos, self.yPos)
            # 왼쪽: clip_composite_draw

