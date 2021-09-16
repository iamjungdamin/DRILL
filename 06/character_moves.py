from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x, y = 100, 90
theta = 270     
shape = 1
direction = 1

while (True):
        
    if (shape == 1):
        clear_canvas_now()
        grass.draw_now(400, 30)

        if (direction == 1):
            character.draw_now(x, y)

            x += 2
            delay(0.01)
            
            if (x > 700):
                direction = 2

        elif (direction == 2):
            character.draw_now(x, y)

            y += 2
            delay(0.01)
            
            if (y > 500):
                direction = 3

        elif (direction == 3):
            character.draw_now(x, y)

            x -= 2
            delay(0.01)

            if (x < 100):
                direction = 4

        elif (direction == 4):
            character.draw_now(x, y)

            y -= 2
            delay(0.01)

            if (y <= 90):
                shape = 2

    elif (shape == 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        
        character.draw_now(x, y)
        
        x = math.cos(theta / 360 * 2 * math.pi) * 200 + 400
        y = math.sin(theta / 360 * 2 * math.pi) * 200 + 300
        theta += 1
        delay(0.01)

        if (theta == 270 + 360):
            shape = 1
            direction = 1
            x, y = 100, 90
            theta = 270

