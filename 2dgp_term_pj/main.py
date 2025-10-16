from pico2d import *
from boy import Boy

open_canvas()
boy = Boy()
running = True

while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        else:
            boy.handle_event(event)
    boy.update()
    clear_canvas()
    boy.draw()
    update_canvas()
    delay(0.03)

close_canvas()
