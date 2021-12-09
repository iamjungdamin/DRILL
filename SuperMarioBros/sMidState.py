import game_framework
from pico2d import *
import sMainState2
import server

name = "MidState"
title = None


def enter():
    global title
    title = load_image('Image/Mid.png')

    server.background = None
    server.mario = None
    server.enemies = []
    server.itemBlocks = []
    server.brickBlocks = []
    server.floorBlocks = []
    server.items = []
    server.pipes = []
    server.flag = None
    server.castle = None

    server.game_time = 150
    server.gaming = True
    server.waiting = 0


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
                game_framework.change_state(sMainState2)


def pause(): pass


def resume(): pass

