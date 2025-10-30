from pico2d import *
import game_framework
import logo_mode
import play_mode
image = None

logo_start_time = 0


def init():
    global image, running, logo_start_time
    image = load_image('title.png')
     pass

def finish():
    global image
    del image


def update():
    clear_canvas()


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)

