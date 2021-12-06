from pico2d import *
import game_framework
import game_world
import server
import collision

import random

import cStage
import cMario
import cEnemy
import cBlock

name = "MainState"
boundingBox = True


def enter():
    server.background = cStage.Background()
    server.mario = cMario.Mario()
    server.enemies = [cEnemy.Goomba(random.randint(400, 800)) for i in range(5)] +\
                     [cEnemy.Turtle(random.randint(400, 800)) for i in range(5)]
    server.itemBlocks = [cBlock.ItemBlock(15 + 6 * 30, 200)]
    server.brickBlocks = [cBlock.BrickBlock(15 + 7 * 30, 200)]
    server.floorBlocks = [cBlock.FloorBlock(15 + i * 30, 15) for i in range(27)] +\
                         [cBlock.FloorBlock(15 + i * 30, 45) for i in range(27)]
    server.flag = cStage.Flag()
    server.castle = cStage.Castle()

    game_world.add_object(server.background, 0)
    game_world.add_object(server.mario, 1)
    game_world.add_objects(server.enemies, 1)
    game_world.add_objects(server.itemBlocks, 0)
    game_world.add_objects(server.brickBlocks, 0)
    game_world.add_objects(server.floorBlocks, 0)
    game_world.add_object(server.flag, 0)
    game_world.add_object(server.castle, 0)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    collision.collide_update()

    for enemy in server.enemies:
        if enemy.die_frame >= 1:
            server.enemies.remove(enemy)
            game_world.remove_object(enemy)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
        if boundingBox:
            game_object.draw_bb()
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
            server.mario.handle_event(event)


def pause(): pass


def resume(): pass

