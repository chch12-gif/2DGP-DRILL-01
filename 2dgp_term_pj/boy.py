from pico2d import *


open_canvas()


ch_sheet = load_image('character_sheet.jpg')


scale = 0.8


frame_w_orig = ch_sheet.w // 3
frame_h_orig = ch_sheet.h

new_width = frame_w_orig * scale
new_height = frame_h_orig * scale

x = 400
y = new_height // 2
speed = 5

# 1-3. 방향 및 상태 변수
dir_x = 0
dir_y = 0
running = True

# 1-4. 애니메이션 및 방향 변수
# 'front':0, 'side':1, 'back':2 (스프라이트 시트의 인덱스)
current_animation_frame_idx = 0
facing_x = 0  # 0: 정면/후면, 1: 오른쪽, -1: 왼쪽 (좌우 뒤집기에 사용)

# --- 2. 게임 루프 ---
while running:
    # 3. 이벤트 처리 (입력)
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

    # 4-1. 캐릭터 애니메이션 프레임 및 방향 결정
    if dir_x == 0 and dir_y == 0:  # 멈춰 있을 때 (정면)
        current_animation_frame_idx = 0  # FRONT
        facing_x = 0  # 정면일 때는 뒤집지 않음
    elif dir_x != 0:  # 좌우로 움직일 때 (옆모습)
        current_animation_frame_idx = 1  # SIDE
        if dir_x > 0:
            facing_x = 1  # 오른쪽
        else:
            facing_x = -1  # 왼쪽
    elif dir_y > 0:  # 위로 움직일 때 (뒷모습)
        current_animation_frame_idx = 2  # BACK
        facing_x = 0  # 뒷모습일 때는 뒤집지 않음
    elif dir_y < 0:  # 아래로 움직일 때 (정면)
        current_animation_frame_idx = 0  # FRONT
        facing_x = 0  # 정면일 때는 뒤집지 않음

    # --- 5. 그리기 (렌더링) ---
    clear_canvas()

    # 스프라이트 시트에서 현재 프레임의 시작 X 좌표 계산
    frame_x_on_sheet = current_animation_frame_idx * frame_w_orig

    # 뒤집기 설정 (facing_x가 -1일 때만 수평 뒤집기)
    flip_option = 'h' if facing_x == -1 else ''

    # clip_composite_draw(소스x, 소스y, 소스w, 소스h, 각도, 뒤집기, 목적x, 목적y, 목적w, 목적h)
    ch_sheet.clip_composite_draw(
        frame_x_on_sheet, 0, frame_w_orig, frame_h_orig,  # 원본 시트에서 자를 영역
        0, flip_option,  # 회전 및 뒤집기
        x, y, new_width, new_height  # 화면에 그릴 위치와 크기
    )

    update_canvas()
    delay(0.01)

# --- 6. 종료 ---
close_canvas()