import game_framework
import game_world
from pico2d import *
import random

import cStage
import cMario
import cEnemy
import cBlock

name = "MainState"
background = None
mario = None
goombas = None
turtles = None
blocks = None


def enter():
    global background, mario, goombas, turtles, blocks
    background = cStage.Stage()
    mario = cMario.Mario()
    goombas = [cEnemy.Goomba(random.randint(500, 600)) for i in range(1)]
    turtles = [cEnemy.Turtle(random.randint(600, 700)) for i in range(1)]
    blocks = [cBlock.ItemBlock(200, 250), cBlock.BrickBlock(170, 250)]

    game_world.add_object(background, 0)
    game_world.add_object(mario, 1)
    game_world.add_objects(goombas, 1)
    game_world.add_objects(turtles, 1)
    game_world.add_objects(blocks, 0)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for goomba in goombas:
        if goomba.die_frame >= 1:
            game_world.remove_object(goomba)
    for turtle in turtles:
        if turtle.die_frame >= 1:
            game_world.remove_object(turtle)

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
    for turtle in turtles:
        if turtle.state == 0 and not mario.invincibility:
            if mario.check_collision(turtle):
                if mario.yPos > turtle.yPos:
                    turtle.state = 1
                else:
                    if mario.trans > 0:
                        mario.trans -= 1
                        # TODO: Game Over
                    mario.invincibility = True
    mario.check_collision(background)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            mario.handle_event(event)


def pause(): pass


def resume(): pass

