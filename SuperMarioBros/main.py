from pico2d import *
from cMario import *
from cGoomba import *


def handle_events(events):
    global gaming
    for event in events:
        if event.type == SDL_QUIT:
            gaming = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            gaming = False


open_canvas()
background = load_image('Image/Background2.png')
mario = Mario()
goomba = Goomba()
gaming = True

while gaming:
    events = get_events()
    handle_events(events)
    mario.input(events)

    mario.update()
    goomba.update()

    clear_canvas()
    background.draw(800/2, 600/2)
    goomba.draw()
    mario.draw()
    update_canvas()

close_canvas()

