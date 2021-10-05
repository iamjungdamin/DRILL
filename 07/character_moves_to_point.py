from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
point = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
px, py = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)
frame = 0
dir = 1  # 1 right, 0 left
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    point.draw(px, py)

    if x < px:
        x += 1
        dir = 1
    if px < x:
        x -= 1
        dir = 0
    if y < py:
        y += 1
    if py < y:
        y -= 1

    if x == px and y == py:
        px, py = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)

    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()

