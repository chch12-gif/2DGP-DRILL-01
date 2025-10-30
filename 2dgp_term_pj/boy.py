from pico2d import *

# --- 1. 초기화 및 기본 설정 ---
open_canvas()

# 1-1. 이미지 로드 (파일 5개 각각 로드)
ch_front = load_image('character.png')
ch_side = load_image('side.png')
ch_back = load_image('back.png')
ch_run_1 = load_image('left_run.png')  # ◀◀ 새로 추가된 달리기 프레임 1
ch_run_2 = load_image('left_run_2.png')  # ◀◀ 새로 추가된 달리기 프레임 2

# 1-2. 크기 및 위치 설정
scale = 0.8  # ◀◀ 크기 비율

# '정면' 이미지를 기준으로 크기 계산
frame_w_orig = ch_front.w
frame_h_orig = ch_front.h

new_width = frame_w_orig * scale
new_height = frame_h_orig * scale

x = 400
y = new_height // 2

# 캐릭터 이동 속도
walk_speed = 5  # 걷는 속도
run_speed = 10  # 뛰는 속도 (Shift 누르면)
current_speed = walk_speed  # 현재 속도

# 1-3. 방향 및 상태 변수
dir_x = 0
dir_y = 0
running_state = False  # ◀◀ Shift 키 눌림 여부 (뛰는 중인지)
animation_frame = 0  # ◀◀ 달리기 애니메이션 프레임 인덱스

running = True
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
            elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # ◀◀ Shift 키 눌림
                running_state = True
                current_speed = run_speed  # 뛰는 속도로 변경
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
            elif event.key == SDLK_LSHIFT or event.key == SDLK_RSHIFT:  # ◀◀ Shift 키 뗐을 때
                running_state = False
                current_speed = walk_speed  # 걷는 속도로 돌아옴

    # --- 4. 논리 계산 (업데이트) ---
    x += dir_x * current_speed  # ◀◀ 현재 속도 사용
    y += dir_y * current_speed  # ◀◀ 현재 속도 사용

    # 4-1. 달리기 애니메이션 프레임 업데이트
    if running_state and (dir_x != 0 or dir_y != 0):  # Shift 누르고 움직일 때
        # 애니메이션 속도를 조절하려면 10 대신 다른 숫자를 곱하세요.
        animation_frame = int(get_time() * 10) % 2  # 2개 프레임(0, 1) 반복
    else:
        animation_frame = 0  # 멈춰있거나 걸을 때는 첫 번째 프레임으로 고정 (선택 사항)

    # --- 5. 그리기 (렌더링) ---
    clear_canvas()

    image_to_draw = ch_front  # 기본값: 정면 서있는 모습
    flip_option = ''  # 기본값: 뒤집지 않음

    # 5-1. 움직임 상태에 따른 이미지 결정
    if dir_x == 0 and dir_y == 0:  # 멈춰 있을 때
        image_to_draw = ch_front
    elif running_state and (dir_x != 0 or dir_y != 0):  # 뛰고 있을 때 (Shift+이동)
        if animation_frame == 0:
            image_to_draw = ch_run_1
        else:
            image_to_draw = ch_run_2

        # 달리는 방향에 따라 이미지 뒤집기 (side.png와 동일하게, 왼쪽을 보고 있다면 원본 사용)
        if dir_x > 0:  # 오른쪽으로 달릴 때
            flip_option = 'h'  # 원본 run 이미지가 왼쪽을 보고 있다면 뒤집기
        elif dir_x < 0:  # 왼쪽으로 달릴 때
            flip_option = ''  # 원본 run 이미지가 왼쪽을 보고 있다면 그대로 사용
        # dir_y로만 움직일 때는 좌우 방향 고정 (예: 위로 뛸 때 앞/뒤 모습의 달리기)
        elif dir_y != 0:
            # 이 부분은 어떻게 처리할지 게임 디자인에 따라 다릅니다.
            # 예시: 이전에 보고 있던 좌우 방향 유지
            # 또는 'run_front.png', 'run_back.png' 같은 이미지가 있다면 사용할 수 있습니다.
            # 여기서는 좌우 움직임이 없으면 flip_option을 초기화합니다.
            flip_option = ''

    elif dir_x != 0:  # 걷고 있을 때 (좌우 이동)
        image_to_draw = ch_side
        if dir_x > 0:  # 오른쪽으로 갈 때 (원본 side.png가 왼쪽을 보고 있으므로 뒤집기)
            flip_option = 'h'
        else:  # 왼쪽으로 갈 때 (원본 side.png 그대로)
            flip_option = ''
    elif dir_y > 0:  # 위로 걸을 때
        image_to_draw = ch_back
    elif dir_y < 0:  # 아래로 걸을 때
        image_to_draw = ch_front

    # 5-2. 선택된 이미지와 옵션으로 그리기
    image_to_draw.composite_draw(
        0, flip_option,  # 회전 및 뒤집기
        x, y, new_width, new_height  # 화면에 그릴 위치와 크기
    )

    update_canvas()
    delay(0.01)

# --- 6. 종료 ---
close_canvas()