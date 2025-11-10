# main.py

from pico2d import *
from boy import Boy

STATE_GAMEPLAY = 0
STATE_VIEWING_ART = 1
current_state = STATE_GAMEPLAY

ART_NONE = 0
ART_MONALISA = 1
ART_STARRY_NIGHT = 2
currently_viewing_art = ART_NONE

current_room_index = 0

mona_x = 100
mona_y = 500
mona_w = 100
mona_h = 150


starry_night_y = 500
starry_night_w = 100
starry_night_h = 150
starry_night_x = mona_x + (mona_w // 2) + (starry_night_w // 2) + 100

interaction_distance = 75

mona_large_w = int(800 * 0.8)
mona_large_h = int(600 * 0.9)

def check_collision(a_x, a_y, b_x, b_y, distance_threshold):
    distance_sq = (a_x - b_x) ** 2 + (a_y - b_y) ** 2
    return distance_sq < distance_threshold ** 2


# --- 1. 초기화 ---
open_canvas(800, 600)


# 1-1. 게임 월드 객체 생성
player = Boy()

# 1-2. 배경 및 사물 로드
background = load_image('BACKGROUND.png')
monalisa_art = load_image('pic_1.png')
starry_night_art = load_image('pic_2.png')

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
                if current_room_index == 0:

                    if check_collision(player.x, player.y, mona_x, mona_y, interaction_distance):
                        current_state = STATE_VIEWING_ART
                        currently_viewing_art = ART_MONALISA

                    elif check_collision(player.x, player.y, starry_night_x, starry_night_y, interaction_distance):
                        current_state = STATE_VIEWING_ART
                        currently_viewing_art = ART_STARRY_NIGHT

            elif current_state == STATE_VIEWING_ART:
                current_state = STATE_GAMEPLAY
                currently_viewing_art = ART_NONE
        else:
            if current_state == STATE_GAMEPLAY:
                player.handle_event(event)
 # 4. 논리 계산 (업데이트)
    if current_state == STATE_GAMEPLAY:
        room_change_status = player.update()

        if room_change_status == 'NEXT':
            current_room_index += 1
            print(f"방 이동: {current_room_index}번 방")
        elif room_change_status == 'PREV':
            current_room_index -= 1
            print(f"방 이동: {current_room_index}번 방")

    # 5. 그리기 (렌더링)
    clear_canvas()

    if current_state == STATE_GAMEPLAY:
       # 5-1. 배경/사물 그리기
       background.draw(400, 300)
       if current_room_index == 0:
           monalisa_art.composite_draw(0, '', mona_x, mona_y, mona_w, mona_h)
           starry_night_art.composite_draw(0, '', starry_night_x, starry_night_y, starry_night_w, starry_night_h)
       elif current_room_index == 1:
           pass

       player.draw()

    # 5-2. 플레이어 그리기

    elif current_state == STATE_VIEWING_ART:
        background.draw(400, 300)
        if currently_viewing_art == ART_MONALISA:
            monalisa_art.composite_draw(0, '', 400, 300, mona_large_w, mona_large_h)
        elif currently_viewing_art == ART_STARRY_NIGHT:
            starry_night_art.composite_draw(0, '', 400, 300, mona_large_w, mona_large_h)

    update_canvas()
    delay(0.01)

# --- 6. 종료 ---
close_canvas()