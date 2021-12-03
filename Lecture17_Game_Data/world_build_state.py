import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

import server

from boy import Boy
from zombie import Zombie


boy = None


name = "WorldBuildState"

menu = None

def enter():
    global menu
    menu = load_image('menu.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass




def create_new_world():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    # zombie_data.json 이라는 초기화 데이터를 사용해서 좀비를 생성, 필요시 데이터만 수정하고 코드 수정x
    with open('zombie_data.json', 'r') as f:    # close 를 안써도 되는 with open 문법 사용
        zombie_data_list = json.load(f)

    for data in zombie_data_list:
        zombie = Zombie(data['name'], data['x'], data['y'], data['size'])
        game_world.add_object(zombie, 1)

def load_saved_world():
    game_world.load()

    for o in game_world.all_objects():
        if isinstance(o, Boy):
            server.boy = o
            break


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load_saved_world()
            game_framework.change_state(main_state)

def update():
    pass

def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update_canvas()






