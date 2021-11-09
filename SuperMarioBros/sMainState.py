import game_framework
from pico2d import *
import random

import cStage
import cMario
import cGoomba

name = "MainState"
background = None
mario = None
goombas = None
boundingBox = True


def enter():
    global background, mario, goombas
    background = cStage.Stage()
    mario = cMario.Mario()
    goombas = [cGoomba.Goomba(random.randint(600, 700)) for i in range(2)]


def exit():
    global background, mario, goombas
    del background
    del mario
    del goombas


def update():
    # global mario, goombas
    mario.update()
    for goomba in goombas:
        goomba.update()
        if goomba.die_frame >= 1:
            goomba.die_frame = 0.0
            goombas.remove(goomba)

    for goomba in goombas:
        if goomba.state == 0 and not mario.invincibility:
            if mario.check_collision(goomba):
                if mario.yPos > goomba.yPos:
                    goomba.state = 1
                else:
                    if mario.trans > 0:
                        mario.trans -= 1
                        # TODO: Game Over
                    mario.invincibility = True
    mario.check_collision(background)


def draw():
    # global background, mario, goombas
    global boundingBox
    clear_canvas()
    background.draw()
    mario.draw()
    for goomba in goombas:
        goomba.draw()

    if boundingBox:
        draw_rectangle(*background.get_bb())
        draw_rectangle(*mario.get_bb())
        for goomba in goombas:
            draw_rectangle(*goomba.get_bb())

    update_canvas()


def handle_events():
    global boundingBox
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            boundingBox = not boundingBox
        else:
            mario.input(events)
            mario.handle_event(event)


def pause(): pass


def resume(): pass

