from pico2d import *
from cMario import *
from cGoomba import *


def handle_events(events):
    global gaming, boundingBox
    for event in events:
        if event.type == SDL_QUIT:
            gaming = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                gaming = False
            if event.key == SDLK_q:
                boundingBox = not boundingBox


def check_collision(a, b):
    a1, a2, a3, a4 = a.get_bb()
    b1, b2, b3, b4 = b.get_bb()

    if a1 > b3 or a3 < b1:  # x축
        return False
    if a4 < b2 or a2 > b4:  # y축
        return False
    # print('Collision', a, b)
    return True


open_canvas()
background = load_image('Image/Background2.png')
mario = Mario()
goomba = Goomba()
gaming = True
boundingBox = True
scrolling = 0

while gaming:
    events = get_events()
    handle_events(events)
    mario.input(events)

    mario.update()
    goomba.update()

    if goomba.state == 0 and not mario.invincibility:
        if check_collision(mario, goomba):
            if mario.yPos > goomba.yPos:
                goomba.state = 1
            elif mario.trans == 2:
                mario.trans = 1
                mario.invincibility = True
    if goomba.state == 0 and not mario.invincibility:
        if check_collision(mario, goomba):
            if mario.yPos > goomba.yPos:
                goomba.state = 1
            elif check_collision(mario, goomba):
                if mario.trans == 1:
                    mario.trans = 0
                    mario.invincibility = True
    # TODO: cMario 안으로 수정
    # TODO: 굼바 완전히 삭제

    # if -1 <= mario.state <= 1:
    #     scrolling += -mario.state
    if scrolling >= 800:
        scrolling = 0

    clear_canvas()
    background.draw(scrolling - 800 / 2, 600 / 2)
    background.draw(scrolling + 800 / 2, 600 / 2)
    goomba.draw()
    mario.draw()

    if boundingBox:
        draw_rectangle(*mario.get_bb())
        if goomba.state == 0:
            draw_rectangle(*goomba.get_bb())

    update_canvas()

close_canvas()
