import random

from pico2d import *
import game_framework


import game_world
import common

from boy import Boy
from court import Court
from ball import Ball


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        else:
            common.boy.handle_event(event)


def init():
    common.court = Court()
    game_world.add_object(common.court, 0)

    # 점수 초기화
    common.score = 0

    # 공 100개 생성 (먼저 추가하여 보이가 위에 렌더링 되도록 함)
    balls = [Ball() for _ in range(100)]
    game_world.add_objects(balls, 1)

    # 보이 생성 및 추가
    common.boy = Boy()
    game_world.add_object(common.boy, 1)

    # 충돌 쌍 등록: 왼쪽에는 보이, 오른쪽에는 각 공들을 개별적으로 추가
    game_world.add_collision_pair('boy:ball', common.boy, None)
    for b in balls:
        game_world.add_collision_pair('boy:ball', None, b)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
