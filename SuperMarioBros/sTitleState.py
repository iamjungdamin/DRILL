import framework
from pico2d import *
import sMainState

name = "TitleState"
title = None


def enter():
    global title
    title = load_image('Image/title.png')


def exit():
    global title
    del title


def update(): pass


def draw():
    global title
    clear_canvas()
    title.draw(800 // 2, 600 // 2)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                framework.quit()
            if event.key == SDLK_SPACE:
                framework.change_state(sMainState)


def pause(): pass


def resume(): pass

