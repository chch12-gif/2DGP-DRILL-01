# main.py

from pico2d import *
from boy import Boy  # ◀◀ 'boy.py' 파일에서 'Boy' 클래스를 가져옵니다.

# --- 1. 초기화 ---
open_canvas(800, 600)

# 1-1. 게임 월드 객체 생성
player = Boy()

# 1-2. 배경 및 사물 로드 (main.py가 관리)
background = load_image('BACKGROUND.png')
monalisa_art = load_image('pic_1.png')
mona_w = 100
mona_h = 150

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
        else:
            # ◀◀ 키 이벤트를 player 객체에게 전달
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