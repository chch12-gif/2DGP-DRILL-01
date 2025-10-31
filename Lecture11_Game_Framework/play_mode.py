from pico2d import *
from boy import Boy
from grass import Grass
import game_world
import game_framework



def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

def finish():
    pass

def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()



open_canvas()
init()
while running:
    handle_events()
    update()
    draw()
    delay(0.01)

    finish()


    def puase():
        pass


    def resume():
        pass
close_canvas()
