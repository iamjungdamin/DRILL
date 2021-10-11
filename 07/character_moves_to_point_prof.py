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


def update_character():
    global x, y
    global ax, ay
    global dir

    if x < ax:
        dir = 1
    else:
        dir = 0

    t = 0.01
    x = (1-t)*x + t*ax
    y = (1-t)*y + t*ay
    # (x, y) 에서 (ax, ay) 로 t씩 접근

    # 캐릭터와 손의 거리 계산
    dist = (ax - x) ** 2 + (ay - y) ** 2
    if dist < 10 ** 2:
        ax, ay = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ax, ay = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)
frame = 0
dir = 1
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
    arrow.draw(ax, ay)
    update_canvas()
    frame = (frame + 1) % 8

    # 캐릭터의 x, y 계산
    update_character()

    handle_events()

close_canvas()

