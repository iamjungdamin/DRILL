from pico2d import *


class Mario:
    def __init__(self):
        self.image = [
            load_image('Image/SmallMario.png'), load_image('Image/BigMario.png'), load_image('Image/FireMario.png')
        ]
        self.xPos = 100
        self.yPos = 83 + 16
        self.frame = 0
        # TODO: enum으로 관리
        self.trans = 0  # SMALL, BIG, FIRE
        self.state = 0  # LEFT, IDLE, RIGHT
        self.jumping = False
        self.attacking = False
        self.invincibility = False
        self.invincibility_frame = 0.0
        self.alpha = 1.0

    def input(self, events):
        for e in events:
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_LEFT:
                    self.state -= 1
                elif e.key == SDLK_RIGHT:
                    self.state += 1
                elif e.key == SDLK_SPACE:
                    self.jump()

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

    def jump(self):
        self.jumping = True
        while self.yPos <= 83 + 16 + 25 * 2:
            self.yPos += 0.5
        self.jumping = False

    def update(self):
        if self.state == 0:
            self.frame = 0
        else:
            self.frame = (self.frame + 1) % 4

        if -1 <= self.state <= 1:
            self.xPos += self.state
        if not self.jumping:
            if self.yPos >= 83 + 16:
                self.yPos -= 0.3

        if self.invincibility:
            self.invincibility_frame += 0.01
            self.alpha = 0.5
            if self.invincibility_frame >= 3:
                self.invincibility_frame = 0.0
                self.invincibility = False
        else:
            self.alpha = 1.0

    def get_bb(self):
        if self.trans == 0:
            w, h = 26, 32
            return self.xPos - w/2, self.yPos - h/2, self.xPos + w/2, self.yPos + h/2
        else:
            w, h = 32, 64
            return self.xPos - w/2, self.yPos - h/2 + 16, self.xPos + w/2, self.yPos + h/2 + 16

    def draw(self):
        if self.state == 0 or self.state == 1:
            if self.trans == 0:
                self.image[self.trans].clip_draw(420 + self.frame * 60, 0, 26, 32, self.xPos, self.yPos)
            elif self.trans == 1:
                self.image[self.trans].clip_draw(416 + self.frame * 60, 0, 32, 64, self.xPos, self.yPos + 16)
            elif self.trans == 2:
                self.image[self.trans].clip_draw(416 + self.frame * 56, 0, 32, 64, self.xPos, self.yPos + 16)
            # TODO: 점프
        if self.state == -1:
            if self.trans == 0:
                self.image[self.trans].clip_composite_draw(420 + self.frame * 60, 0, 26, 32, 0, 'h', self.xPos, self.yPos, 26, 32)
            elif self.trans == 1:
                self.image[self.trans].clip_composite_draw(416 + self.frame * 60, 0, 32, 64, 0, 'h', self.xPos, self.yPos + 16, 32, 64)
            elif self.trans == 2:
                self.image[self.trans].clip_composite_draw(416 + self.frame * 56, 0, 32, 64, 0, 'h', self.xPos, self.yPos + 16, 32, 64)
        self.image[self.trans].opacify(self.alpha)

    def check_collision(self, obj):
        a1, a2, a3, a4 = self.get_bb()
        b1, b2, b3, b4 = obj.get_bb()

        if a1 > b3 or a3 < b1:  # x축
            return False
        if a4 < b2 or a2 > b4:  # y축
            return False
        return True

