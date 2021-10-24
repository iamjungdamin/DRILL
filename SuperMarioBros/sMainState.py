import framework
from pico2d import *
import cMario
import cGoomba

name = "MainState"
background = None
mario = None
goomba = None
boundingBox = True


def enter():
    global background, mario, goomba
    background = load_image('Image/background2.png')
    mario = cMario.Mario()
    goomba = cGoomba.Goomba()


def exit():
    global background, mario, goomba
    del background
    del mario
    del goomba


def update():
    global mario, goomba
    mario.update()
    goomba.update()

    if goomba.state == 0 and not mario.invincibility:
        if check_collision(mario, goomba):
            if mario.yPos > goomba.yPos:
                goomba.state = 1
            else:
                if mario.trans == 2:
                    mario.trans = 1
                    mario.invincibility = True
                elif mario.trans == 1:
                    mario.trans = 0
                    mario.invincibility = True
                elif mario.trans == 0:
                    # TODO: Game Over
                    pass


def draw():
    global background, mario, goomba
    global boundingBox
    clear_canvas()
    background.draw(800 / 2, 600 / 2)
    mario.draw()
    goomba.draw()

    if boundingBox:
        draw_rectangle(*mario.get_bb())
        draw_rectangle(*goomba.get_bb())

    update_canvas()


def handle_events():
    global boundingBox
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                framework.quit()
            if event.key == SDLK_q:
                boundingBox = not boundingBox
    mario.input(events)


def pause(): pass


def resume(): pass


def check_collision(a, b):
    a1, a2, a3, a4 = a.get_bb()
    b1, b2, b3, b4 = b.get_bb()

    if a1 > b3 or a3 < b1:  # x축
        return False
    if a4 < b2 or a2 > b4:  # y축
        return False
    return True

