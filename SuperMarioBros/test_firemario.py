from pico2d import *

open_canvas()

running = True
image = load_image('Image/FireMario.png')
frame = 0

while running:
    clear_canvas()

    events = get_events()
    for e in events:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                frame -= 1
            elif e.key == SDLK_RIGHT:
                frame += 1
            elif e.key == SDLK_ESCAPE:
                running = False

    image.clip_draw(416 + frame * 51, 0, 32, 64, 400, 300)
    update_canvas()

close_canvas()

