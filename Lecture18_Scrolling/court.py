from pico2d import load_image, get_canvas_width, get_canvas_height, clamp
import common

class Court:
    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h


    def update(self):
        self.window_left = clamp(0, int(common.boy.x)- self.cw//2, self.w - self.cw -1)
        self.window_bottom = clamp(0, int(common.boy.y)- self.ch//2, self.h - self.ch -1)
        pass

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)



class TileCourt:
    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()

        # 타일 맵을 3x3 타일로 구성한 유한 월드
        self.tile_w = self.image.w
        self.tile_h = self.image.h
        self.cols = 3
        self.rows = 3
        self.w = self.tile_w * self.cols
        self.h = self.tile_h * self.rows


    def update(self):
        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def draw(self):
        # 윈도우 좌표 계산
        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, self.h - self.ch - 1)

        # 그려야 할 타일 인덱스 범위 계산
        start_i = self.window_left // self.tile_w
        end_i = (self.window_left + self.cw) // self.tile_w
        start_j = self.window_bottom // self.tile_h
        end_j = (self.window_bottom + self.ch) // self.tile_h

        for i in range(start_i, end_i + 1):
            for j in range(start_j, end_j + 1):
                if 0 <= i < self.cols and 0 <= j < self.rows:
                    # 스크린 좌표
                    sx = i * self.tile_w - self.window_left
                    sy = j * self.tile_h - self.window_bottom
                    # 전체 타일 이미지를 해당 위치에 그림
                    self.image.draw_to_origin(sx, sy)


class InfiniteCourt:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        # 무한 타일링: 화면을 덮을 만큼 이미지들을 반복해서 그림
        start_x = int(common.boy.x) - self.cw // 2
        start_y = int(common.boy.y) - self.ch // 2

        # 이미지에서의 오프셋
        ox = start_x % self.w
        oy = start_y % self.h

        # 필요한 타일 수
        nx = self.cw // self.w + 2
        ny = self.ch // self.h + 2

        for ix in range(nx):
            for iy in range(ny):
                screen_x = ix * self.w - ox
                screen_y = iy * self.h - oy
                # 이미지를 전체 크기로 그리면 화면 밖은 자동으로 잘림
                self.image.draw_to_origin(screen_x, screen_y)

    def update(self):
        # update는 draw에서 사용하는 start 오프셋을 update할 필요 없음
        # 기존 구조와의 호환성을 위해 값들을 계산해두긴 하지만 draw에서 직접 계산함
        # quadrant 3
        self.q3l = (int(common.boy.x) - self.cw // 2) % self.w
        self.q3b = (int(common.boy.y) - self.ch // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)
        # quadrant 2
        self.q2l = 0
        self.q2b = self.q3b
        self.q2w = clamp(0, self.cw - self.q3w, self.w)
        self.q2h = self.q3h
        # quadrand 4
        self.q4l = self.q3l
        self.q4b = 0
        self.q4w = self.q3w
        self.q4h = clamp(0, self.ch - self.q3h, self.h)
        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q2w
        self.q1h = self.q4h


    def handle_event(self, event):
        pass
