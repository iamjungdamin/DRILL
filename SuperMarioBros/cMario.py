from pico2d import *
import game_framework
import game_world
import server
import collision


PIXEL_PER_METER = (30.0 / 0.3)  # 30 pixel 30 cm
RUN_SPEED_KMPH = 3.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, CTRL = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL
}


class IdleState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.frame = 0

    def exit(mario, event):
        if event == SPACE:
            mario.jump()
        elif event == CTRL:
            if mario.trans == 2:
                mario.attack()

    def do(mario):
        pass

    def draw(mario):
        pass


class RunState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
        if event == SPACE:
            mario.jump()
        elif event == CTRL:
            if mario.trans == 2:
                mario.attack()

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        mario.xPos += mario.velocity * game_framework.frame_time

    def draw(mario):
        pass


next_state_table = {
    IdleState: {RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: RunState, LEFT_UP: RunState,
                SPACE: IdleState, CTRL: IdleState},
    RunState: {RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, RIGHT_UP: IdleState, LEFT_UP: IdleState,
               SPACE: RunState, CTRL: RunState}
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
        self.dir = 1
        self.velocity = 0
        self.fall_speed = 0

        self.invincibility = False
        self.invincibility_frame = 0.0
        self.alpha = 1.0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_0):
            self.trans = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            self.trans = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            self.trans = 2
        elif (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        self.yPos += -1 * self.fall_speed
        self.fall_speed += 1
        delay(0.01)

        if self.invincibility:
            self.invincibility_frame += game_framework.frame_time
            self.alpha = 0.5
            if self.invincibility_frame >= 1:
                self.invincibility_frame = 0.0
                self.invincibility = False
        else:
            self.alpha = 1.0

        for enemy in server.enemies:
            if enemy.state == 0 and not self.invincibility:
                if collision.check_collision(self, enemy):
                    if self.yPos > enemy.yPos:
                        enemy.state = 1
                        self.jump()
                        # break
                    else:
                        if self.trans > 0:
                            self.trans -= 1
                            # TODO: Game Over
                        self.invincibility = True
                        break

        if collision.check_collision(self, server.background):
            self.fall_speed = 0
            self.yPos = server.background.yPos - 300 + 83 + 16

        for block in server.itemBlocks:
            if collision.check_collision(self, block):
                self.fall_speed = 0
                self.yPos = block.yPos + 15 + 16
            if collision.check_collision(self, block, 0, 1):
                block.frame = 3
                # self.fall_speed = 0
                self.yPos = block.yPos - 15 - 16
        for block in server.brickBlocks:
            if collision.check_collision(self, block):
                self.fall_speed = 0
                self.yPos = block.yPos + 15 + 16
            if collision.check_collision(self, block, 0, 1):
                server.brickBlocks.remove(block)
                game_world.remove_object(block)
                # self.fall_speed = 0
                self.yPos = block.yPos - 15 - 16

    def jump(self):
        self.frame = 5
        if self.trans == 2:
            self.frame = 6
        # if self.fall_speed == 0:
        self.fall_speed = -15

    def attack(self):
        self.frame = 4
        # TODO: 파이어볼

    def get_bb(self, bb_type=0):
        if self.trans == 0:
            w, h = 26, 32
            return self.xPos - w/2, self.yPos - h/2, self.xPos + w/2, self.yPos + h/2
        else:
            w, h = 32, 64
            return self.xPos - w/2, self.yPos - h/2 + 16, self.xPos + w/2, self.yPos + h/2 + 16

    def draw(self):
        # self.cur_state.draw(self)
        if self.dir == 1:
            if self.trans == 0:
                self.image[self.trans].clip_draw(420 + int(self.frame) * 60, 0, 26, 32, self.xPos, self.yPos)
            elif self.trans == 1:
                self.image[self.trans].clip_draw(416 + int(self.frame) * 60, 0, 32, 64, self.xPos, self.yPos + 16)
            elif self.trans == 2:
                self.image[self.trans].clip_draw(416 + int(self.frame) * 51, 0, 32, 64, self.xPos, self.yPos + 16)
        else:
            if self.trans == 0:
                self.image[self.trans].clip_composite_draw(420 + int(self.frame) * 60, 0, 26, 32, 0, 'h',
                                                           self.xPos, self.yPos, 26, 32)
            elif self.trans == 1:
                self.image[self.trans].clip_composite_draw(416 + int(self.frame) * 60, 0, 32, 64, 0, 'h',
                                                           self.xPos, self.yPos + 16, 32, 64)
            elif self.trans == 2:
                self.image[self.trans].clip_composite_draw(416 + int(self.frame) * 51, 0, 32, 64, 0, 'h',
                                                           self.xPos, self.yPos + 16, 32, 64)
        self.image[self.trans].opacify(self.alpha)

        draw_rectangle(*self.get_bb())
        debug_print('V:' + str(self.velocity) + '  D:' + str(self.dir) + ' S:' + str(self.cur_state.__name__))

