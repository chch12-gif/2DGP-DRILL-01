import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            if boy is not None:
                boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_collision_pairs('grass:grass', grass, None)

    boy = Boy()
    game_world.add_object(boy, 1)

    # 초기에는 발사된 공 없음; 소년이 발사할 때만 공이 생성되어 충돌테이블에 추가됨
    global balls
    balls = []
    # 충돌 그룹에 boy와 grass는 왼쪽으로 등록해둠
    game_world.add_collision_pairs('boy:ball', boy, None)
    game_world.add_collision_pairs('grass:ball', grass, None)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)


def update():
    game_world.update()
    # collision_pairs에 등록해둔 모든 충돌 그룹 처리
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass
