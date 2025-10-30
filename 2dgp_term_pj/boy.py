from pico2d import *

# --- 1. 초기화 및 기본 설정 ---
open_canvas()

# 1-1. 이미지 로드 (파일 3개 각각 로드)
ch_front = load_image('character.png')
ch_side = load_image('side.png')
ch_back = load_image('back.png')

# 1-2. 크기 및 위치 설정
scale = 0.8 # ◀◀ 크기 비율

# '정면' 이미지를 기준으로 크기 계산
frame_w_orig = ch_front.w
frame_h_orig = ch_front.h

new_width = frame_w_orig * scale
new_height = frame_h_orig * scale

x = 400
y = new_height // 2 # ◀◀ 줄어든 높이 기준으로 y좌표 설정
speed = 5

# 1-3. 방향 및 상태 변수
dir_x = 0
dir_y = 0
running = True

# --- 2. 게임 루프 ---
while running:
    # 3. 이벤트 처리 (입력) - 이전과 동일
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

    # --- 4. 논리 계산 (업데이트) ---
    x += dir_x * speed
    y += dir_y * speed

    # --- 5. 그리기 (렌더링) ---
    clear_canvas()

    # 5-1. 상황에 따라 그릴 이미지와 뒤집기 옵션 결정
    image_to_draw = ch_front  # 기본값은 정면
    flip_option = ''          # 기본값은 뒤집지 않음

    if dir_x == 0 and dir_y == 0: # 멈춰 있을 때
        image_to_draw = ch_front
    elif dir_x != 0: # 좌우로 움직일 때
        image_to_draw = ch_side
        if dir_x > 0: # 오른쪽으로 갈 때 (원본이 왼쪽을 보니 '뒤집기')
            flip_option = 'h'
        else: # 왼쪽으로 갈 때 (원본 '그대로')
            flip_option = ''
    elif dir_y > 0: # 위로 움직일 때
        image_to_draw = ch_back
    elif dir_y < 0: # 아래로 움직일 때
        image_to_draw = ch_front

    # 5-2. 선택된 이미지와 옵션으로 그리기
    # composite_draw(각도, 뒤집기, 화면x, 화면y, 화면너비, 화면높이)
    image_to_draw.composite_draw(
        0, flip_option,           # 회전 및 뒤집기
        x, y, new_width, new_height # 화면에 그릴 위치와 크기
    )

    update_canvas()
    delay(0.01)

# --- 6. 종료 ---
close_canvas()