from pico2d import *


open_canvas()

ch = load_image('character.png')
x = 400
y = ch.h // 2  # 캐릭터의 바닥이 화면 바닥에 오도록 y좌표 설정
speed = 5      # 캐릭터 이동 속도

dir_x = 0  # 수평 방향 (기존 dir 변수 -> dir_x로 변경)
dir_y = 0  # 수직 방향 (새로 추가)

running = True # 게임 루프 실행 여부

# 2. 게임 루프
while running:
    # 3. 이벤트 처리 (입력)
    events = get_events()
    for event in events:
        # 창 닫기 버튼을 눌렀을 때
        if event.type == SDL_QUIT:
            running = False
        # 키보드 키가 눌렸을 때
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:    # ◀◀ 새로 추가
                dir_y += 1
            elif event.key == SDLK_DOWN:  # ◀◀ 새로 추가
                dir_y -= 1
            elif event.key == SDLK_ESCAPE: # ESC 키로 종료
                running = False
        # 키보드 키에서 손을 뗐을 때
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:    # ◀◀ 새로 추가
                dir_y -= 1
            elif event.key == SDLK_DOWN:  # ◀◀ 새로 추가
                dir_y += 1

    # 4. 논리 계산 (캐릭터 위치 업데이트)
    x += dir_x * speed  # ◀◀ dir_x 사용
    y += dir_y * speed  # ◀◀ y 좌표 업데이트 추가

    # 5. 그리기 (렌더링)
    clear_canvas()   # 배경 지우기
    ch.draw(x, y)    # 캐릭터 그리기
    update_canvas()  # 화면에 최종 출력

    delay(0.01)      # 아주 잠깐 대기

# 6. 종료
close_canvas()