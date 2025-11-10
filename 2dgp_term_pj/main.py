# main.py

from pico2d import *
from boy import Boy

STATE_GAMEPLAY = 0
STATE_VIEWING_ART = 1
current_state = STATE_GAMEPLAY

mona_x = 100
mona_y = 500
mona_w = 100
mona_h = 150
interaction_distance = 75

def check_collision(a_x, a_y, b_x, b_y, distance_threshold):
    distance_sq = (a_x - b_x) ** 2 + (a_y - b_y) ** 2
    return distance_sq < distance_threshold ** 2


# --- 1. 초기화 ---
open_canvas(800, 600)

# 1-1. 게임 월드 객체 생성
player = Boy()

# 1-2. 배경 및 사물 로드 (main.py가 관리)
background = load_image('BACKGROUND.png')
monalisa_art = load_image('pic_1.png')


running = True

# --- 2. 게임 루프 ---
while running:
    # 3. 이벤트 처리
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            if current_state == STATE_GAMEPLAY:
                if check_collision(player.x, player.y, mona_x, mona_y, interaction_distance):
                    current_state = STATE_VIEWING_ART
            elif current_state == STATE_VIEWING_ART:
                current_state = STATE_GAMEPLAY
        else:
            if current_state == STATE_GAMEPLAY:
                player.handle_event(event)
            # 4. 논리 계산 (업데이트)
    player.update()

    # 5. 그리기 (렌더링)
    clear_canvas()

    # 5-1. 배경/사물 그리기
    background.draw(400, 300)
    monalisa_art.composite_draw(0, '', 100, 500, mona_w, mona_h)

    # 5-2. 플레이어 그리기
    player.draw()

    update_canvas()
    delay(0.01)

# --- 6. 종료 ---
close_canvas()