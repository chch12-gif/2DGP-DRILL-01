from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
charcter = load_image('character.png')


left, right, bottom, top = 50, 750, 90, 550
center_x, center_y, radius = 400, 300, 210

while True:

    for x in range(left, right + 1, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        charcter.draw_now(x, bottom)
        delay(0.01)

    for y in range(bottom, top + 1, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        charcter.draw_now(right, y)
        delay(0.01)

    for x in range(right, left - 1, -2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        charcter.draw_now(x, top)
        delay(0.01)

    for y in range(top, bottom - 1, -2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        charcter.draw_now(left, y)
        delay(0.01)


    for degree in range(360, 0, -2):
        rad = math.radians(degree)
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)
        clear_canvas_now()
        grass.draw_now(400, 30)
        charcter.draw_now(int(x), int(y))
        delay(0.01)

close_canvas()
