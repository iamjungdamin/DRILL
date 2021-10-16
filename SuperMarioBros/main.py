from pico2d import *


def handle_events():
    global gaming
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gaming = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            gaming = False


# TODO: 클래스 분리
class Mario:
    def __init__(self):
        self.image = load_image('Image/Mario.png')
        self.xPos = 100
        self.yPos = 100
        self.frame = 0
        # TODO: enum으로 state 관리

    def update(self):
        # self.frame = (self.frame + 1) % 4

        events = get_events()
        for e in events:
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_LEFT:
                    self.xPos -= 5
                elif e.key == SDLK_RIGHT:
                    self.xPos += 5

    def draw(self):
        self.image.clip_draw(420, 376 - 32, 28, 32, self.xPos, self.yPos)
        # TODO: if state == ... clip_draw


open_canvas()
background = load_image('Image/Background.png')
mario = Mario()
gaming = True

while gaming:
    handle_events()
    # mario.update()

    clear_canvas()
    background.draw(800/2, 600/2)
    mario.draw()
    update_canvas()

close_canvas()