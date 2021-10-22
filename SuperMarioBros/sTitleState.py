import framework
from pico2d import *


name = "TitleState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Image/title.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        framework.quit()
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(800 / 2, 600 / 2)
    update_canvas()


def handle_events():
    events = get_events()


def pause(): pass


def resume(): pass


