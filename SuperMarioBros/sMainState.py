from pico2d import *
import game_framework
import game_world
import server
import collision

import cStage
import cMario
import cEnemy
import cBlock

name = "MainState"
boundingBox = True


def enter():
    cStage.setup()
    server.mario = cMario.Mario()
    cEnemy.setup()
    cBlock.setup()

    game_world.add_object(server.background, 0)
    game_world.add_object(server.mario, 1)
    game_world.add_objects(server.enemies, 1)
    game_world.add_objects(server.itemBlocks, 0)
    game_world.add_objects(server.brickBlocks, 0)
    game_world.add_objects(server.floorBlocks, 0)
    game_world.add_objects(server.pipes, 0)
    game_world.add_object(server.flag, 0)
    game_world.add_object(server.castle, 0)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    server.game_time -= game_framework.frame_time
    collision.collide_update()

    if server.mario.check_win():
        pass
    else:
        pass
        # server.mario.die_sound.play()

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

