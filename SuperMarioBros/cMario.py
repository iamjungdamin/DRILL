from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class IdleState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += 1
        elif event == LEFT_DOWN:
            mario.velocity -= 1
        elif event == RIGHT_UP:
            mario.velocity -= 1
        elif event == LEFT_UP:
            mario.velocity += 1
        mario.frame = 0

    def exit(mario, event):
        pass

    def do(mario):
        pass

    def draw(mario):
        if mario.state == 1:    # facing right
            if mario.trans == 0:
                mario.image[mario.trans].clip_draw(420 + mario.frame * 60, 0, 26, 32, mario.xPos, mario.yPos)
            elif mario.trans == 1:
                mario.image[mario.trans].clip_draw(416 + mario.frame * 60, 0, 32, 64, mario.xPos, mario.yPos + 16)
            elif mario.trans == 2:
                mario.image[mario.trans].clip_draw(416 + mario.frame * 51, 0, 32, 64, mario.xPos, mario.yPos + 16)
        else:
            if mario.trans == 0:
                mario.image[mario.trans].clip_composite_draw(420 + mario.frame * 60, 0, 26, 32, 0, 'h',
                                                             mario.xPos, mario.yPos, 26, 32)
            elif mario.trans == 1:
                mario.image[mario.trans].clip_composite_draw(416 + mario.frame * 60, 0, 32, 64, 0, 'h',
                                                             mario.xPos, mario.yPos + 16, 32, 64)
            elif mario.trans == 2:
                mario.image[mario.trans].clip_composite_draw(416 + mario.frame * 51, 0, 32, 64, 0, 'h',
                                                             mario.xPos, mario.yPos + 16, 32, 64)
        mario.image[mario.trans].opacify(mario.alpha)


class RunState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += 1
        elif event == LEFT_DOWN:
            mario.velocity -= 1
        elif event == RIGHT_UP:
            mario.velocity -= 1
        elif event == LEFT_UP:
            mario.velocity += 1
        mario.state = mario.velocity

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + 1) % 4
        mario.xPos += mario.velocity

    def draw(mario):
        if mario.velocity == 1:
            if mario.trans == 0:
                mario.image[mario.trans].clip_draw(420 + mario.frame * 60, 0, 26, 32, mario.xPos, mario.yPos)
            elif mario.trans == 1:
                mario.image[mario.trans].clip_draw(416 + mario.frame * 60, 0, 32, 64, mario.xPos, mario.yPos + 16)
            elif mario.trans == 2:
                mario.image[mario.trans].clip_draw(416 + mario.frame * 51, 0, 32, 64, mario.xPos, mario.yPos + 16)
        else:
            if mario.trans == 0:
                mario.image[mario.trans].clip_composite_draw(420 + mario.frame * 60, 0, 26, 32, 0, 'h',
                                                             mario.xPos, mario.yPos, 26, 32)
            elif mario.trans == 1:
                mario.image[mario.trans].clip_composite_draw(416 + mario.frame * 60, 0, 32, 64, 0, 'h',
                                                             mario.xPos, mario.yPos + 16, 32, 64)
            elif mario.trans == 2:
                mario.image[mario.trans].clip_composite_draw(416 + mario.frame * 51, 0, 32, 64, 0, 'h',
                                                             mario.xPos, mario.yPos + 16, 32, 64)
        mario.image[mario.trans].opacify(mario.alpha)


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: RunState, LEFT_UP: RunState},
    RunState: {RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, RIGHT_UP: IdleState, LEFT_UP: IdleState}
}


class Mario:
    def __init__(self):
        self.image = [
            load_image('Image/SmallMario.png'), load_image('Image/BigMario.png'), load_image('Image/FireMario.png')
        ]
        self.xPos = 100
        self.yPos = 83 + 16
        self.frame = 0
        self.trans = 0  # SMALL, BIG, FIRE
        self.state = 0  # LEFT, IDLE, RIGHT
        self.velocity = 0

        self.jumping = False
        self.fall_speed = 0

        self.attacking = False
        self.invincibility = False
        self.invincibility_frame = 0.0
        self.alpha = 1.0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def input(self, events):
        for e in events:
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_SPACE:
                    self.jump()

                # TODO: 변신 아이템, 몬스터와 충돌 시 변신
                elif e.key == SDLK_0:
                    self.trans = 0
                elif e.key == SDLK_1:
                    self.trans = 1
                elif e.key == SDLK_2:
                    self.trans = 2

    def jump(self):
        self.jumping = True
        self.fall_speed = -15

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        self.yPos += -1 * self.fall_speed
        self.fall_speed += 1
        delay(0.005)
        if self.jumping:
            if self.trans == 2:
                self.frame = 6
            else:
                self.frame = 5

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
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.state))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def check_collision(self, obj):
        a1, a2, a3, a4 = self.get_bb()
        b1, b2, b3, b4 = obj.get_bb()

        if a1 > b3 or a3 < b1:  # x축
            return False
        if a4 < b2 or a2 > b4:  # y축
            return False

        if obj.type == 'enemy':
            # self.jump()
            pass
        elif obj.type == 'ground':
            self.fall_speed = 0
            self.jumping = False
            self.yPos = b4 + 16
        return True

