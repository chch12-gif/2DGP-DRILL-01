from pico2d import *
import game_framework
import play_mode

def handle_events():
events = get_events()
for event in events:
    if event.type == SDL_QUIT:
        game_framework.quit()
    elif event.type == SDL_KEYDOWN:
         match event.key:
         case pico2d.SDLK_ESCAPE:
              game_framework.pop_mode()
         case pico2d.SDLK_0:
              play_mode.boy.item = None
              game_framework.pop_mode()
         case pico2d.SDLK_1:
              play_mode.boy.item = 'Ball'
              game_framework.pop_mode()
         case pico2d.SDLK_2:
              play_mode.boy.item = 'BigBall'
              game_framework.pop_mode()


def pause():
    pass
def resume():
    pass
