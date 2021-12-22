import game_framework
from pico2d import *
import sMainState
import sMainState2
import server

name = "MidState"
title = None


def enter():
    global title
    title = load_image('Image/Mid.png')
    server.init_game()


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
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_SPACE:
                if server.cur_stage == 1:
                    game_framework.change_state(sMainState)
                elif server.cur_stage == 2:
                    game_framework.change_state(sMainState2)


def pause(): pass


def resume(): pass

