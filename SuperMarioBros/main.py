from pico2d import *
from cMario import *


def handle_events():
    global gaming
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gaming = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            gaming = False


open_canvas()
background = load_image('Image/Background.png')
mario = Mario()
gaming = True

while gaming:
    # handle_events()
    mario.update()

    clear_canvas()
    background.draw(800/2, 600/2)
    mario.draw()
    update_canvas()

close_canvas()

