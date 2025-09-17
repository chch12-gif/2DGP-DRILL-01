from pico2d import *
import math

def move_character(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    charcter.draw_now(int(x), int(y))
    delay(0.01)

# 사각형 운동: 시작점에서 반시계 방향으로 한 바퀴, 마지막 좌표 반환
# 시작점에서 가장 가까운 변부터 시작
# 사각형 좌표: 좌하(left, bottom), 좌상(left, top), 우상(right, top), 우하(right, bottom)
def square_motion(start_x, start_y):
    points = [(left, bottom), (left, top), (right, top), (right, bottom)]
    # 시작점에서 가장 가까운 꼭짓점 찾기
    dists = [math.hypot(start_x-p[0], start_y-p[1]) for p in points]
    start_idx = dists.index(min(dists))
    # 꼭짓점 순서 재정렬
    ordered = points[start_idx:] + points[:start_idx]
    # 각 변을 따라 이동
    for i in range(4):
        x0, y0 = ordered[i]
        x1, y1 = ordered[(i+1)%4]
        for t in range(0, 101, 2):
            x = x0 + (x1-x0)*t/100
            y = y0 + (y1-y0)*t/100
            move_character(x, y)
    return ordered[0]  # 마지막 좌표 반환

# 삼각형 운동: 시작점에서 가장 가까운 꼭짓점부터 반시계 방향으로 한 바퀴, 마지막 좌표 반환
def triangle_motion(start_x, start_y):
    points = [tri_p1, tri_p2, tri_p3]
    dists = [math.hypot(start_x-p[0], start_y-p[1]) for p in points]
    start_idx = dists.index(min(dists))
    ordered = points[start_idx:] + points[:start_idx]
    for i in range(3):
        x0, y0 = ordered[i]
        x1, y1 = ordered[(i+1)%3]
        for t in range(0, 101, 2):
            x = x0 + (x1-x0)*t/100
            y = y0 + (y1-y0)*t/100
            move_character(x, y)
    return ordered[0]

# 원 운동: 시작점에서 가장 가까운 각도부터 시계 방향으로 한 바퀴, 마지막 좌표 반환
def circle_motion(start_x, start_y):
    # 시작점에서 원 중심까지의 각도 계산
    dx = start_x - center_x
    dy = start_y - center_y
    start_angle = math.degrees(math.atan2(dy, dx))
    if start_angle < 0:
        start_angle += 360
    for degree in range(int(start_angle), int(start_angle)+360, 2):
        rad = math.radians(degree)
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)
        move_character(x, y)
    # 마지막 좌표 반환
    rad = math.radians(start_angle+358)
    x = center_x + radius * math.cos(rad)
    y = center_y + radius * math.sin(rad)
    return (x, y)

open_canvas()
grass = load_image('grass.png')
charcter = load_image('character.png')

left, right, bottom, top = 50, 750, 90, 550
center_x, center_y, radius = 400, 300, 210
tri_p1 = (400, 550)
tri_p2 = (750, 90)
tri_p3 = (50, 90)

# 초기 시작점(사각형 좌하)
x, y = left, bottom
while True:
    x, y = square_motion(x, y)
    x, y = triangle_motion(x, y)
    x, y = circle_motion(x, y)

close_canvas()