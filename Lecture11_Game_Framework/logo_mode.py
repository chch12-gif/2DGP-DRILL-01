from pico2d import *
import game_framework
import title_mode



image = None

logo_start_time = 0


def init():
    global image, running, logo_start_time
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()
    pass

def finish():
    global image
    del image


def update():
    clear_canvas()
    if get_time() - logo_start_time > 2.0:
       game_framework.change_mode(title_mode)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    #no nothing

